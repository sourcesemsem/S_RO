#🗿روجر كان هنا
import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from ..Config import Config

from ..helpers.utils import reply_id
from .sql_helper.globals import gvarstatus
from resources.strings import *
from . import ALIVE_NAME, StartTime, get_readable_time, mention
from . import reply_id as rd


def check_data_base_heal_th():
    is_database_working = False
    output = "لــم يــتــم تــعــيــيــن قــاعــدة بــيــانــات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "تــعــمــل بــنــجــاح"
        is_database_working = True
    return is_database_working, output


@bot.on(admin_cmd(outgoing=True, pattern="فحص$"))
@bot.on(sudo_cmd(pattern="فحص$", allow_sudo=True))
async def baqiralive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "**⎆┊جـاري .. فحـص البـوت الخـاص بك**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    Z_EMOJI = Config.CUSTOM_ALIVE_EMOJI or "⎆┊"
    ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "**بـوت ريبـــثون 𝗥𝗘𝗣𝗧𝗛𝗢𝗡 يعمـل .. بنجـاح ☑️ 𓆩**"
    ZZL_IMG = Config.ALIVE_PIC or "https://graph.org/file/615da9bbf808580163ca4.jpg"
    Ralls_caption = Config.Ralls_MEDIA or Rallsmp
    caption = Ralls_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        repver="3.1.3",
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if ZZL_IMG:
        ZZL = [x for x in ZZL_IMG.split()]
        PIC = random.choice(ZZL)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**⎆┊هنـالك خطـأ بـ رابـط الميديـا **\n⎆┊قم بتغييـر الرابـط باستخـدام الامـر  \n⎆┊ `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**⎆┊لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


Rallsmp = """{ALIVE_TEXT}

**{Z_EMOJI} قاعدۿ البيانات :** تعمل بنـجاح
**{Z_EMOJI} إصـدار التـيليثون :** `{telever}`
**{Z_EMOJI} إصـدار ريبـــثون :** `{repver}`
**{Z_EMOJI} إصـدار البـايثون :** `{pyver}`
**{Z_EMOJI} الوقـت :** `{uptime}`
**{Z_EMOJI} المسـتخدم:** {mention}
**{Z_EMOJI} قنـاة السـورس :** [اضغـط هنـا](https://t.me/Repthon)"""
