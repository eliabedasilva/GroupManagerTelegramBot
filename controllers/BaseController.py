import telebot

class BaseController:
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot
