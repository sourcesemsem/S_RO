from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from ...utils import errors_handler
from .. import BOTLOG, BOTLOG_CHATID, extract_time, get_user_from_event

# =================== CONSTANT ===================
NO_ADMIN = "⪼ **أنا لست مشرف هنا!!** 𓆰."
NO_PERM = "⪼ **ليس لدي أذونات كافية!** 𓆰."


@zedthon.on(zelzal_cmd(pattern=r"اكتم(?: |$)(.*)"))
@zedthon.on(sudo_cmd(pattern=r"اكتم(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def tmuter(zelzal):
    chat = await zelzal.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(zelzal, NO_ADMIN)
        return
    zede = await edit_or_reply(zelzal, "╮ ❐ جـاري الڪتم 𓅫╰")
    user, reason = await get_user_from_event(zelzal, zede)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        zedt = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await zede.edit("you haven't mentioned time, check `.info tadmin`")
        return
    self_user = await zelzal.client.get_me()
    itime = await extract_time(zelzal, zedt)
    if not itime:
        await zede.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {zedt}"
        )
        return
    if user.id == self_user.id:
        await zede.edit(f"**⪼ لا استطيـع كتم نفسـي 𓆰،**")
        return
    try:
        await zede.client(
            EditBannedRequest(
                zelzal.chat_id,
                user.id,
                ChatBannedRights(until_date=itime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await zede.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} was muted in {zelzal.chat.title}\n"
                f"**Muted for : **{zedt}\n"
                f"**Reason : **__{reason}__"
            )
            if BOTLOG:
                await zelzal.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{zelzal.chat.title}(`{zelzal.chat_id}`)\n"
                    f"**Muted for : **`{zedt}`\n"
                    f"**Reason : **`{reason}``",
                )
        else:
            await zede.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} was muted in {zelzal.chat.title}\n"
                f"Muted for {zedt}\n"
            )
            if BOTLOG:
                await zelzal.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{zelzal.chat.title}(`{zelzal.chat_id}`)\n"
                    f"**Muted for : **`{zedt}`",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await zede.edit("`Uh oh my mute logic broke!`")
    except UserAdminInvalidError:
        return await zede.edit(
            "`Either you're not an admin or you tried to mute an admin that you didn't promote`"
        )
    except Exception as e:
        return await zede.edit(f"`{str(e)}`")


@zedthon.on(zelzal_cmd(pattern="احظر(?: |$)(.*)"))
@zedthon.on(sudo_cmd(pattern="احظر(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def ban(zelzal):
    chat = await zelzal.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(zelzal, NO_ADMIN)
        return
    zede = await edit_or_reply(zelzal, "╮ ❐ جـاري الحـظࢪ ❏╰")
    user, reason = await get_user_from_event(zelzal, zede)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        tosh = len(reason)
        zedt = reason[0]
        reason = reason[1] if tosh == 2 else None
    else:
        await zede.edit("you haven't mentioned time, check `.info tadmin`")
        return
    self_user = await zelzal.client.get_me()
    itime = await extract_time(zelzal, zedt)
    if not itime:
        await zede.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {zedt}"
        )
        return
    if user.id == self_user.id:
        await zede.edit(f"**⪼ لا استطيـع حظر نفسـي 𓆰،**")
        return
    await zede.edit("`Whacking the pest!`")
    try:
        await zelzal.client(
            EditBannedRequest(
                zelzal.chat_id,
                user.id,
                ChatBannedRights(until_date=itime, view_messages=True),
            )
        )
    except UserAdminInvalidError:
        return await zede.edit(
            "`Either you're not an admin or you tried to ban an admin that you didn't promote`"
        )
    except BadRequestError:
        await zede.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await zelzal.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await zede.edit("`I dont have message nuking rights! But still he was banned!`")
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await zede.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} was banned in {zelzal.chat.title}\n"
            f"banned for {zedt}\n"
            f"Reason:`{reason}`"
        )
        if BOTLOG:
            await zelzal.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{zelzal.chat.title}(`{zelzal.chat_id}`)\n"
                f"**Banned untill : **`{zedt}`\n"
                f"**Reason : **__{reason}__",
            )
    else:
        await zede.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} was banned in {zelzal.chat.title}\n"
            f"banned for {zedt}\n"
        )
        if BOTLOG:
            await zelzal.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{zelzal.chat.title}(`{zelzal.chat_id}`)\n"
                f"**Banned untill : **`{zedt}`",
            )


CMD_HELP.update(
    {
        "الادمن مؤقت": "**Plugin :** `الادمن مؤقت`\
      \n\n•  **Syntax : **`.اكتم <reply/username/userid> <time> <reason>`\
      \n•  **Function : **__Temporary mutes the user for given time.__\
      \n\n•  **Syntax : **`.احظر <reply/username/userid> <time> <reason>`\
      \n•  **Function : **__Temporary bans the user for given time.__\
      \n\n•  **Time units : ** __(2m = 2 minutes) ,(3h = 3hours)  ,(4d = 4 days) ,(5w = 5 weeks)\
      These times are example u can use anything with those units __"
    }
)
