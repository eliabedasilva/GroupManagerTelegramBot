import telebot

class BaseView:
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot

    def show_menu(self):
        ...