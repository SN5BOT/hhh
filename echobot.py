from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import random

BOTidSBot=Client(
    "Pyrogram Bot", 
    bot_token="5131732775:AAGBIP8WByqCGeiO-bElbvc7XbjS_P1l7_0", 
    api_id="13472617", 
    api_hash="deb30aa6abbfca7d4cdffaec397edbc1"
)

ALL_PIC = [
 "https://te.legra.ph/file/869985eff0bf4b3d545d8.jpg",
 "https://te.legra.ph/file/579444763df09f4a59b6b.jpg"
]

ALL_VIDEO = [
 "https://te.legra.ph/file/a6becafdb6bccfc0bc71e.mp4"
]

@BOTidSBot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
    await message.reply_video(
        video=random.choice(ALL_VIDEO),
        caption="Hello",
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
