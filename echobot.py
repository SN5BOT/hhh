from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

BOTidSBot=Client(
    "Pyrogram Bot", 
    bot_token="5131732775:AAGBIP8WByqCGeiO-bElbvc7XbjS_P1l7_0", 
    api_id="13472617", 
    api_hash="deb30aa6abbfca7d4cdffaec397edbc1",
    BOT_USERNAME="@S6nsbot"
)

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
   


@BOTidSBot.on_callback_query()
async def cb_handler(client, query):

    if query.data == "id":
        await query.answer()
        await query.message.edit_text(
            ID_TEXT.format(query.from_user.id)
        )
        return

    elif query.data == "close":




        await query.message.delete()
    ID_TEXT = """
🖤🥀 𝚈𝙾𝚄𝚁 𝚃𝙴𝙻𝙴𝚁𝙰𝙼 𝙸𝙳 𝙸𝚂 ➻ <code>{}</code>
"""

BOTidSBot.run()
