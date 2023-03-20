#𝙍𝙀𝙋𝙏𝙃𝙊𝙉 ®
#الملـف حقـوق وكتابـة روجر⤶ @E_7_V خاص بسـورس ⤶ 𝙍𝙀𝙋𝙏𝙃𝙊𝙉


#هههههههههههههههههه


from telethon import events
from telethon.tl.types import InputMessagesFilterPhotos

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="بنت ?(.*)"))
@bot.on(sudo_cmd(pattern="بنت ?(.*)", allow_sudo=True))
async def _(event):
    rrevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        repph = [
            roger
            async for roger in event.client.iter_messages(
                "@shhdhn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(repph),
            caption=f"**◞افتـارات آنمي بنـات ➧🎆🧚🏻‍♀◟**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](https://t.me/Repthon)",
        )
        await rrevent.delete()
    except Exception:
        await rrevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

CMD_HELP.update(
    {
        "انمي بنات": "**اسم الاضافـه : **`انمي بنات`\
    \n\n**╮•❐ الامـر ⦂ **`..بنت انمي`  \
    \n**الشـرح •• **اكثـر مـن 1000 افتـارات انمـي بنـات ممطـروقـه .. ارسـل ..بنت انمي"
    }
)
