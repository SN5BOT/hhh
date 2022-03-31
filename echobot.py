import requests
import pyfiglet
from os import getenv
from pyrogram import Client, filters
from googletrans import Translator


bot = Client("chatbot", 
                bot_token=getenv("BOT_TOKEN")
                api_id=getenv("API_ID"), 
                api_hash=getenv("API_HASH"))
tr = Translator()


@bot.on_message(filters.command("start"))
async def startmsg(_, message):
    await message.reply_video(video="https://telegra.ph/file/b8f0cbdf67943328459d2.mp4", 
    caption=f"Hello {message.from_user.mention}. \nI'm AI Chat bot made by Tinura Dinith by Using Affiliateplus API, You can chat with me here.")

@bot.on_message(
    filters.text 
    & filters.private 
    & ~filters.edited 
    & ~filters.bot 
    & ~filters.channel 
    & ~filters.forwarded,
    group=1)
async def chatbot(_, message):
    if message.text[0] == "/":
        return
@bot.message_handler(func=lambda message:True)
def name(message):
    name = message.text
    design = pyfiglet.figlet_format(name)
    bot.send_message(message.chat.id,text=design)
bot.run()
