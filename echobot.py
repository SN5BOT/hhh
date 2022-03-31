from pyrogram import Client, filters
from googletrans import Translator
from pyrogram.types
import pyfiglet
import telebot
from googletrans import Translator

bot = Client("Chatbot", 
                bot=getenv("telebot.TeleBot")

tr = Translator()


@bot.message_handler(commands=['start'])
def first_msg(message):
    bot.send_message(message.chat.id,text=f'<b>Hi {message.from_user.first_name}\n- - - - - - - -\nWelcome To Terminal Name Bot\nSend Your Name To Make It\n- - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html')
@bot.message_handler(func=lambda message:True)
def name(message):
    name = message.text
    design = pyfiglet.figlet_format(name)
    bot.send_message(message.chat.id,text=design)
bot.run()
