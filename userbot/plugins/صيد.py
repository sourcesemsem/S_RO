# by: t.me/Dar4k  ~ t.me/E_7_V

import asyncio
import random

import requests
import telethon
from telethon.sync import functions
from . import *

from userbot import bot


a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

trys, trys2 = [0], [0]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    elif choice == "سداسي":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        # random.shuffle(f)
        username = "".join(f)
        username = username + "bot"

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)

        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        return "error"
    return username


@bot.on(admin_cmd(pattern="الصيد"))
@bot.on(sudo_cmd(pattern="الصيد", allow_sudo=True))
async def _(event):
    await event.edit(
        """
أوامــر الــصــيــد الــخــاصــة بــســورس ريبـــثون : 

ٴ— — — — — — — — — —

النوع :(  سداسي حرفين/ ثلاثي/ سداسيات/ بوتات/ خماسي حرفين/خماسي /سباعي )

الامر:  `.صيد` + النوع
- يقوم بصيد معرفات عشوائية حسب النوع

الامر:  `تثبيت` + معرف
* وظيفة الامر : يقوم بالتثبيت على المعرف عندما يصبح متاح يأخذه

ٴ— — — — — — — — — —
الامر:   `.حالة الصيد`
• لمعرفة عدد المحاولات للصيد

الامر:  `.حالة التثبيت`
• لمعرفة عدد المحاولات للصيد

**@Repthon - channel userbot**

"""
    )


@bot.on(admin_cmd(pattern="صيد (.*)"))
@bot.on(admin_cmd(pattern="الصيد", allow_sudo=True))
async def hunterusername(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء الصيد في @{ch} .")
    except:
        try:
            ch = await bot(
                functions.channels.CreateChannelRequest(
                    title="REPTHON HUNTER - صيد جمثون",
                    about="This channel to hunt username by - @Repthon ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
        except Exception as e:
            await bot.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
            )
    delgvar("isclaim")
    addgvar("isclaim", "True")
    for i in range(19000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يرجى وضع النوع بشكل صحيح**.")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await bot(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n- By : @E_7_V - @Repthon !\n- Hunting Log {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await bot.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await bot.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys[0] += 1
    delgvar("isclaim")
    await event.client.send_message(event.chat_id, "**- تم بنجاح الانتهاء من الصيد**")


@bot.on(admin_cmd(pattern="تثبيت (.*)"))
@bot.on(sudo_cmd(pattern="تثبيت", allow_sudo=True))
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await bot(
                functions.channels.CreateChannelRequest(
                    title="REPTHON HUNTER - صيد ريبـــثون",
                    about="This channel to hunt username by - @Repthon ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await bot.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    delgvar("isauto")
    addgvar("isauto", "True")
    username = str(msg[1])

    for i in range(1000000000000):
        isav = check_user(username)
        if isav == True:
            try:
                await bot(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n- By : @E_7_V - @Repthon !\n- Hunting Log {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                break
            except telethon.errors.FloodError as e:
                await bot.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await bot.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                break
        else:
            pass
        trys2[0] += 1

        await asyncio.sleep(1.3)
    delgvar("isauto")
    await bot.send_message(event.chat_id, "**- تم الانتهاء من التثبيت بنجاح**")


@bot.on(admin_cmd(pattern="حالة الصيد"))
@bot.on(sudo_cmd(pattern="حالة الصيد", allow_sudo=True))
async def _(event):
    if gvarstatus("isclaim"):
        await event.edit(f"**- الصيد وصل لـ({trys[0]}) **من المحاولات")
    elif gvarstatus("isclaim") is None:
        await event.edit("**- الصيد بالاصل لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@bot.on(admin_cmd(pattern="حالة التثبيت"))
@bot.on(admin_cmd(pattern="حالة التثبيت", allow_sudo=True))
async def _(event):
    if gvarstatus("isauto"):
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif gvarstatus("isauto") is None:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
