#    Icss - Userbot
#    Owner - @zlzzl77

from telethon import events, Button
from ..Config import Config
from . import TOSH, K, mention


@asst_cmd("/repo|#repo")
async def dev(kimo):
    await kimo.reply(
        "⌔∮ 𝙎𝙊𝙐𝙍𝘾𝙀 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝙍𝙀𝙋𝙊 𓆪",
        buttons=[[Button.url("🔗 𝙍𝙀𝙋𝙊 🔗", K)]]
    )
   

TOSH_PIC = Config.ALIVE_PIC if Config.ALIVE_PIC else "https://telegra.ph/file/f72cde9805f01e0bf04ed.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await bot.get_me()
        if query.startswith("فحص") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("الرابـط 🔗", K),
                    Button.url("قنـاة السـورس ⚙️", "https://t.me/ZedThon"),
                ]
            ]
            if TOSH_PIC and TOSH_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    TOSH_PIC,
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False
                )
            elif TOSH_PIC:
                result = builder.document(
                    TOSH_PIC,
                    title="ICSS - USERBOT",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="ICSS - USERBOT",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="فحص"))
async def repo(event):
    if event.fwd_from:
        return
    KIM = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(KIM, "فحص")
    await response[0].click(event.chat_id)
    await event.delete()

