from pyrogram import Client, filters


JESUS=Client(
    "Pyrogram Bot", 
    bot_token=getenv("BOT_TOKEN"), 
    api_id=getenv("API_ID"), 
    api_hash=getenv("API_HASH"))

)


@JESUS.on_message(filters.command("start"))
async def startmsg(bot, message):
    await message.reply_video(video="https://telegra.ph/file/b8f0cbdf67943328459d2.mp4", 
    caption=f"Hello")



bot.run()
