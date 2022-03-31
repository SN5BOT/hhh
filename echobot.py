from pyrogram import Client, filters

from time import sleep
from user_agent import generate_user_agent

bot=Client(
    "Pyrogram Bot", 
    bot_token="5131732775:AAGBIP8WByqCGeiO-bElbvc7XbjS_P1l7_0", 
    api_id="13472617", 
    api_hash="deb30aa6abbfca7d4cdffaec397edbc1"
)

@bot.on_message(filters.command("start"))
async def startmsg(bot, message):
    await message.reply_video(video="https://telegra.ph/file/b8f0cbdf67943328459d2.mp4", 
    caption=f"Hello")


    msg = message.text
    url = f"http://apis.xditya.me/write?text={msg}"
    bot.send_photo(message.chat.id,url,caption=f"<strong>Done\n@us7a5</strong>",parse_mode="html")

bot.run()
