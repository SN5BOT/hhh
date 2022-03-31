from os import getenv
from pyrogram import Client, filters
from googletrans import Translator


bot = Client("yes", 
                bot_token=getenv("BOT_TOKEN")

tr = Translator()


@bot.on_message(filters.command("start"))
async def startmsg(_, message):
    bot.send_message(message.chat.id,text=f'<b>Hi {message.from_user.first_name}\n- - - - - - - -\nWelcome To Terminal Name Bot\nSend Your Name To Make It\n- - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html')
@bot.message_handler(func=lambda message:True)
def name(message):
    name = message.text
    design = pyfiglet.figlet_format(name)
    bot.send_message(message.chat.id,text=design)
bot.run()
