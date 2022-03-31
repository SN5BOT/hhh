from pyrogram import Client, filters
from pyrogram.tyoes import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
bot=Client(
    "Pyrogram Bot", 
    bot_token="5131732775:AAGBIP8WByqCGeiO-bElbvc7XbjS_P1l7_0", 
    api_id="13472617", 
    api_hash="deb30aa6abbfca7d4cdffaec397edbc1"
)

@bot.on_message(filters.command("start"))
async def startmsg(bot, message):
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("channel", url=f"https://t.me/robloxXO")
                 ]]
                )
            )

    await message.reply_text("hello")
    

bot.run()
