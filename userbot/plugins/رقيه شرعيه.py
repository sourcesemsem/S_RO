#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣


#صدقـة جـاريـه لـروح المرحومـة أمـي وروح المرحومـة أم مـلاذ


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="رقيه ?(.*)"))
@bot.on(sudo_cmd(pattern="رقيه ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . اكثـر من 200 رقيـه شرعيـه .. صـدقه جـاريـه 𓅫╰**"
        )
    chat = "@ZlZZl77bot"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرقيـه الشـرعيه ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1956894280)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZlZZl77bot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "رقيه شرعيه": "**اسم الاضافـه : **`رقيه شرعيه`\
    \n\n**╮•❐ الامـر ⦂ **`.رقيه شرعيه`  \
    \n**الشـرح •• **اكثـر مـن 200 رقيـه شرعيـه .. اللهـم اجعلهـا صدقـة جـاريـه"
    }
)
