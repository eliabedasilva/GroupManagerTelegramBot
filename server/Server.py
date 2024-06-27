import telebot, ngrok
from flask import Flask, request

from credentials import NGROK_AUTHTOKEN, TELEGRAM_TOKEN

NGROK_URL = ngrok.forward(5000, authtoken=NGROK_AUTHTOKEN).url()

bot = telebot.TeleBot(TELEGRAM_TOKEN)

bot.remove_webhook()
bot.set_webhook(url=f'{NGROK_URL}/{TELEGRAM_TOKEN}')

# Manipulador de atualizações recebidas pelo webhook
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Olá! Esta é uma resposta do seu bot.")

# Use o Flask apenas para evitar que o script termine
app = Flask(__name__)

@app.route('/' + TELEGRAM_TOKEN, methods=['POST'])
def webhook_handler():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return '', 200


def main():
    app.run(port=5000)


if __name__ == '__main__':
    main()
    