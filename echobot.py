from pyrogram import Client, filters

bot=Client(
    "Pyrogram Bot", 
    bot_token="5131732775:AAGBIP8WByqCGeiO-bElbvc7XbjS_P1l7_0", 
    api_id="13472617", 
    api_hash="deb30aa6abbfca7d4cdffaec397edbc1"
)

@bot.on_message(filters.command("start"))
async def startmsg(bot, message):
    await message.reply_photo(photo="https://te.legra.ph/file/869985eff0bf4b3d545d8.jpg", 
    caption=f"Hello")


bot.run()
