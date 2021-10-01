#ZedThon
#حقوق زد ثـون_تخمط اذكـر المصـدر حمبـي
#@zzzzl1l
import asyncio
import base64
import os
import random
import time
from datetime import datetime
from io import BytesIO

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from PIL import Image
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.functions.messages import SendMediaRequest

from . import make_gif, progress
from . import reply_id

if not os.path.isdir("./temp"):
    os.makedirs("./temp")


@bot.on(admin_cmd(pattern="متحرك$", outgoing=True))
@bot.on(sudo_cmd(pattern="متحرك$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الفيديـو حمبـي 🧸🎈```**")
        return
    chat = "@SYRAPK_CONVERTBOT"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحـويل ... 🧸🎆**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1546534674)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "`RIP Check Your Blacklist Boss and unblock @TIKTOKDOWNLOADROBOT`"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("Am I Dumb Or Am I Dumb?")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "متحرك": "**اسم الاضافـه : **`متحرك`\
    \n\n**╮•❐ الامـر ⦂ **`.متحرك` بالرد على الفيـديـو\
    \n**الشـرح •• **تحميل مقاطـع الفيديـو من متحـركـه"
    }
)
