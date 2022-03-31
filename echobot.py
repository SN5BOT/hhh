from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


BOTidSBot=Client(
    "Pyrogram Bot", 
    bot_token="******:AAGBIP8WByqCGeiO******XbjS_P1l7_0", 
    api_id="*****7", 
    api_hash="de******7d4cdffa*****edbc1"
)

@BOTidSBot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text="links ♛",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Button1", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button2", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button3", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button4", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button5", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button6", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button7", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button8", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button9", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button10", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button11", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button12", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button13", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button14", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button15", url=f"t.me/us7a5")
            ]]
            )
        )
   

BOTidSBot.run()
