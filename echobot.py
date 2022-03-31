from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


@BOTidSBot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text="links",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Button1", callback_data="id"),
            InlineKeyboardButton("Button2", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button3", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button4", url=f"t.me/us7a5")
            ],[
            InlineKeyboardButton("Button5", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button6", url=f"t.me/us7a5"),
            InlineKeyboardButton("Button7", url=f"t.me/us7a5")
            ]]
            )
        )
   

BOTidSBot.run()
