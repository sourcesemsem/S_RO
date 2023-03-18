#Repthon ®
#الملـف حقـوق وكتابـة روجر⤶ @ZQ_LO خاص بسـورس ⤶ 𝗥𝗲𝗽𝘁𝗵𝗼𝗻


#هههههههههههههههههه


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import InputMessagesFilterVideo 

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ستوري ?(.*)"))
@bot.on(sudo_cmd(pattern="ستوري ?(.*)", allow_sudo=True))
async def _(event):
    rrevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الستـوري ...**")
    try:
        REPTHON = [
            roger
            async for roger in event.client.iter_messages(
                "@AA_Zll", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(REPTHON),
            caption=f"**🎆┊ستـوريات آنمـي قصيـرة 🖤🧧**\n\n[➧𝙎𝙤𝙪𝙧𝙘𝙚 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](https://t.me/Repthon)",
        )
        await rrevent.delete()
    except Exception:
        await rrevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
CMD_HELP.update(
    {
        "انمي ستوري": "**اسم الاضافـه : **`انمي ستوري`\
    \n\n**╮•❐ الامـر ⦂ **`.ستوري انمي`  \
    \n**الشـرح •• **اكثـر مـن 1000 ستـوريات انمـي قصيـرة ممطـروقـه .. ارسـل .ستوري انمي"
    }
)
