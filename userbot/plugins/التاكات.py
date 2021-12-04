#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®

import re
import asyncio
import base64
import string
import os
import subprocess
import io
import sys
import traceback
from datetime import datetime
from asyncio import sleep
from geopy.geocoders import Nominatim
from gtts import gTTS
from telethon import custom, events
from telethon.tl import types, functions, types
from telethon.errors import rpcbaseerrors
from telethon.tl.types import Channel, MessageMediaWebPage, ChatBannedRights
from telethon import Button
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from random import choice, randint
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.utils import get_display_name
from googletrans import LANGUAGES, Translator
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterEmpty, InputMessagesFilterGeo, InputMessagesFilterGif, InputMessagesFilterMusic, InputMessagesFilterPhotos, InputMessagesFilterRoundVideo, InputMessagesFilterUrl, InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterMyMentions, InputMessagesFilterPinned     
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from ..Config import Config
from ..helpers.tools import media_type
from ..helpers.utils import _icssutils, parse_pre
from ..helpers import reply_id
from .sql_helper.globals import addgvar, delgvar, gvarstatus
from .sql_helper.welcome_sql import add_welcome_setting, get_current_welcome_settings, rm_welcome_setting, update_previous_welcome
from .sql_helper.echo_sql import addecho, get_all_echos, is_echo
from .sql_helper.filter_sql import add_filter, get_filters, remove_all_filters, remove_filter
from .sql_helper import antiflood_sql as sql
from .sql_helper import blacklist_sql as sql1
from ..utils import is_admin
from . import BOTLOG, BOTLOG_CHATID, get_user_from_event, deEmojify, reply_id
CHAT_FLOOD = sql.__load_flood_settings()
ANTI_FLOOD_WARN_MODE = ChatBannedRights(
until_date=None, view_messages=None, send_messages=True)
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")

def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
@bot.on(admin_cmd(pattern="كتابه وهمي(?:\s|$)([\s\S]*)"))
async def _zed(zedthon):
    zed = zedthon.pattern_match.group(1)
    if not (zed or zed.isdigit()):
        zed = 100
    else:
        try:
            zed = int(zed)
        except BaseException:
            try:
                zed = await zedthon.ban_time(zed)
            except BaseException:
                return await event.edit("**اكتب الامر بشكل صحيح**")
    await zedthon.edit(f"**❈╎تم بـدء وضـع الكتابـه الوهميـه لـ {zed} من الثوانـي**")
    async with zedthon.client.action(zedthon.chat_id, "typing"):
        await asyncio.sleep(zed)
@bot.on(admin_cmd(pattern="فيديو وهمي(?:\s|$)([\s\S]*)"))
async def _zed(zedthon):
    zed = zedthon.pattern_match.group(1)
    if not (zed or zed.isdigit()):
        zed = 100
    else:
        try:
            zed = int(zed)
        except BaseException:
            try:
                zed = await zedthon.ban_time(zed)
            except BaseException:
                return await event.edit("**اكتب الامر بشكل صحيح**")
    await zedthon.edit(f"**تم بدء وضع فيديو وهمي لـ {zed} من الثوانـي**")
    async with zedthon.client.action(zedthon.chat_id, "record-video"):
        await asyncio.sleep(zed)
@bot.on(admin_cmd(pattern="صوت وهمي(?:\s|$)([\s\S]*)"))
async def _zed(zedthon):
    zed = zedthon.pattern_match.group(1)
    if not (zed or zed.isdigit()):
        zed = 100
    else:
        try:
            zed = int(zed)
        except BaseException:
            try:
                zed = await zedthon.ban_time(zed)
            except BaseException:
                return await event.edit("**اكتب الامر بشكل صحيح**")
    await zedthon.edit(f"**تم بدء وضع صوت وهمي لـ {zed} من الثوانـي**")
    async with zedthon.client.action(zedthon.chat_id, "record-audio"):
        await asyncio.sleep(zed)
@bot.on(admin_cmd(pattern="لعب وهمي(?:\s|$)([\s\S]*)"))
async def _zed(zedthon):
    zed = zedthon.pattern_match.group(1)
    if not (zed or zed.isdigit()):
        zed = 100
    else:
        try:
            zed = int(zed)
        except BaseException:
            try:
                zed = await zedthon.ban_time(zed)
            except BaseException:
                return await event.edit("**اكتب الامر بشكل صحيح**")
    await zedthon.edit(f"**تم بدء وضع لعب وهمي لـ {zed} من الثوانـي**")
    async with zedthon.client.action(zedthon.chat_id, "game"):
        await asyncio.sleep(zed)  
@bot.on(admin_cmd(pattern="موقع وهمي(?:\s|$)([\s\S]*)"))
async def _zed(zedthon):
    zed = zedthon.pattern_match.group(1)
    if not (zed or zed.isdigit()):
        zed = 100
    else:
        try:
            zed = int(zed)
        except BaseException:
            try:
                zed = await zedthon.ban_time(zed)
            except BaseException:
                return await event.edit("**اكتب الامر بشكل صحيح**")
    await zedthon.edit(f"**تم بدء وضع موقع وهمي لـ {zed} من الثوانـي**")
    async with zedthon.client.action(zedthon.chat_id, "location"):
        await asyncio.sleep(zed)
@bot.on(admin_cmd(pattern="جهه اتصال وهمي(?:\s|$)([\s\S]*)"))
async def _zed(zedthon):
    zed = zedthon.pattern_match.group(1)
    if not (zed or zed.isdigit()):
        zed = 100
    else:
        try:
            zed = int(zed)
        except BaseException:
            try:
                zed = await zedthon.ban_time(zed)
            except BaseException:
                return await event.edit("**اكتب الامر بشكل صحيح**")
    await zedthon.edit(f"**تم بدء وضع جهه اتصال وهمي لـ {zed} من الثوانـي**")
    async with zedthon.client.action(zedthon.chat_id, "contact"):
        await asyncio.sleep(zed)  
@bot.on(admin_cmd(pattern="معرفات 100(?: |$)(.*)"))
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 100):
        mentions += f"\n**-** @{x.username} "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@bot.on(admin_cmd(pattern="معرفات 200(?: |$)(.*)"))
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 200):
        mentions += f"\n**-** @{x.username} "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@bot.on(admin_cmd(pattern="تاك 200(?: |$)(.*)"))
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 200):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@bot.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 150):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@bot.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 100):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@bot.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 50):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) "
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@bot.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def zed(zedthon):
    mentions = zedthon.text[8:]
    chat = await zedthon.get_input_chat()
    async for x in zedthon.client.iter_participants(chat, 10):
        mentions += f"\n**𒀭╎**  [{x.first_name}](tg://user?id={x.id}) \n"
    await zedthon.client.send_message(zedthon.chat_id, mentions)
    await zedthon.delete()
@bot.on(admin_cmd(pattern="احسب ([\s\S]*)"))    
async def calculator(event):
    cmd = event.text.split(" ", maxsplit=1)[1]
    event = await edit_or_reply(event, "**✾╎جـاري حسـاب المسـئلـة 📐**")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "**✾╎عـذار المسـئلة لااقـدر حلـها أو هنـاك خطـأ بتـرتيـب السـؤال 🆘**"
    final_output = "**✾╎المسئلة **: `{}` \n **✾╎الجواب **: `{}` \n".format(cmd, evaluation)
    await event.edit(final_output)

async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)
@bot.on(admin_cmd(pattern="ابلاغ الادمنيه(?: |$)(.*)"))    
async def zed(event):
    mentions = "@تاك للادمنيه : **✾╎تم رصـد إزعـاج ⚠️**"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()
@bot.on(admin_cmd(incoming=True))
async def on_new_message(event):
    name = event.raw_text
    snips = sql1.get_chat_blacklist(event.chat_id)
    catadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    if not catadmin:
        return
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.client.send_message(BOTLOG_CHATID, f"  ليس لدي إذن حذف\n {get_display_name(await event.get_chat())}.لأزاله الكلمات الممنوعه ")
                for word in snips:
                    sql1.rm_from_blacklist(event.chat_id, word.lower())
            break
@bot.on(admin_cmd(pattern="منع(?:\s|$)([\s\S]*)"))    
async def _(event):
    text = event.pattern_match.group(1)
    to_blacklist = list({trigger.strip() for trigger in text.split("\n") if trigger.strip()})

    for trigger in to_blacklist:
        sql1.add_to_blacklist(event.chat_id, trigger.lower())
    await edit_or_reply(event, "**⌔︙ تم اضافة {} الكلمة في قائمة المنع بنجاح ✅**".format(len(to_blacklist)),)
@bot.on(admin_cmd(pattern="الغاء منع(?:\s|$)([\s\S]*)"))    
async def _(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list({trigger.strip() for trigger in text.split("\n") if trigger.strip()})
    successful = sum(
        bool(sql1.rm_from_blacklist(event.chat_id, trigger.lower()))
        for trigger in to_unblacklist)
    await edit_or_reply(event, f"تم حذف   {successful} / {len(to_unblacklist)} من قائمه المنع")
@bot.on(admin_cmd(pattern="قائمه المنع$"))    
async def _(event):
    all_blacklisted = sql1.get_chat_blacklist(event.chat_id)
    OUT_STR = "الكلمات الممنوعه هنا :\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"👉 {trigger} \n"
    else:
        OUT_STR = "لم يتم العثور على كلمات ممنوعه . ابدأ في منع كلمات باستخدام `.منع + الكلمه`"
    await edit_or_reply(event, OUT_STR)
@bot.on(admin_cmd(pattern="تاك بالكلام ([\s\S]*)"))    
async def zed(event):
    user, input_str = await get_user_from_event(event)
    if not user:
        return
    reply_to_id = await reply_id(event)
    await event.delete()
    await event.client.send_message(event.chat_id, f"<a href='tg://user?id={user.id}'>{input_str}</a>", parse_mode="HTML", reply_to=reply_to_id)
