from pyrogram import filters
from pyrogram.types import Message

from ShioriXMusic import app
from ShioriXMusic.Cache.getid import *


@app.on_message(
    filters.command(["id", "stickerid", "stkid", "stckrid"]))
async def showid(_, message: Message):
    chat_type = message.chat.type
    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>ᴄʜᴀᴛ ɪᴅ</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>ᴜsᴇʀ ɪᴅ</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
