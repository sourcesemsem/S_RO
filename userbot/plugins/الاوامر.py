# commands for source Repthon by ~ @ZQ_LO


import random
from ..tosh import Cmds
from telethon import events

@bot.on(admin_cmd(pattern="الاوامر"))
@bot.on(sudo_cmd(pattern="الاوامر", allow_sudo=True))
async def cmds(Roger):
    await eor(Roger, Cmds)

########################  SOURCE Repthon ~ BY: ZQ_LO (@Repthon)  ########################


import random

from telethon import events

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م1":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝑹𝐸𝑃𝑇𝐻𝑂𝑁 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝑹𝐸𝑃𝑇𝐻𝑂𝑁](t.me/Repthon) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝑹𝐸𝑃𝑇𝐻𝑂𝑁 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝑹𝐸𝑃𝑇𝐻𝑂𝑁](t.me/Repthon) 𓆪"
            )

########################  SOURCE REPTHON ~ BY: ZQ_LO@ (@Repthon)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م2":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝑹𝐸𝑃𝑇𝐻𝑂𝑁 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر التسليه :** \n\n⪼ `.شرح تسليه` \n⪼ `.شرح تسليه1` \n⪼ `.شرح تسليه2` \n⪼ `.شرح تسليه3` \n⪼ `.شرح تسليه4` \n⪼ `.شرح تسليه5` \n⪼ `.شرح تسليه7` \n⪼ `.شرح تسليه8` \n\n**- جديـده :**\n\n⪼ `.شرح تسليه9` \n⪼ `.شرح تسليه10` \n\n\n**⌔╎قائـمه اوامر التسليه الجديده حقـوق سـورس ريبـــثون:**\n\n⪼ `.كشف` \nبالـرد / المعرف/ الايدي \n**امـر تسـليه كشـف حيـوان 😂🐴**\n\n⪼ `.مشهور`\n بالـرد /المعرف /الايدي\n**امـر تسـليه زوجنـي من مشهـور 👨‍⚖💍** \n\n⪼ `.مشهوره`\n بالرد /المعرف /الايدي \n **امـر تسـليه زوجنـي من مشهـوره 👰🏻‍♀💍**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝑹𝐸𝑃𝑇𝐻𝑂𝑁 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر التسليه :** \n\n⪼ `.شرح تسليه` \n⪼ `.شرح تسليه1` \n⪼ `.شرح تسليه2` \n⪼ `.شرح تسليه3` \n⪼ `.شرح تسليه4` \n⪼ `.شرح تسليه5` \n⪼ `.شرح تسليه7` \n⪼ `.شرح تسليه8` \n\n**- جديـده :**\n\n⪼ `.شرح تسليه9` \n⪼ `.شرح تسليه10` \n\n\n**⌔╎قائـمه اوامر التسليه الجديده حقـوق سـورس ريبـــثون:**\n\n⪼ `.كشف` \nبالـرد / المعرف/ الايدي \n**امـر تسـليه كشـف حيـوان 😂🐴**\n\n⪼ `.مشهور`\n بالـرد /المعرف /الايدي\n**امـر تسـليه زوجنـي من مشهـور 👨‍⚖💍** \n\n⪼ `.مشهوره`\n بالرد /المعرف /الايدي \n **امـر تسـليه زوجنـي من مشهـوره 👰🏻‍♀💍**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪"
            )

########################  SOURCE 𝐑𝐀𝐈𝐈𝐒𝙏𝙃𝙊𝙉 ~ BY: QQ070 (@RallsThon)  ########################


import random

from telethon import events

@bot.on(sudo_cmd(pattern="م3", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE 𝐑𝐀𝐈𝐈𝐒𝙏𝙃𝙊𝙉 ~ BY: QQ070 (@RallsThon)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م3":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝑹𝐸𝑃𝑇𝐻𝑂𝑁 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 [𝑺𝑶𝑼𝑹𝑪𝑬 𝑹𝐸𝑃𝑇𝐻𝑂𝑁 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪"
            )

########################  SOURCE 𝐑𝐀𝐈𝐈𝐒𝙏𝙃𝙊𝙉 ~ BY: QQ070 (@RallsThon)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م4"))
@bot.on(sudo_cmd("م4", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الردود :** \n⪼ `.اضف رد ` الامر ثم اسم الرد بالرد ع كلمة الرد \n⪼ `.حذف رد ` \n⪼ `.حذف الردود `\n⪼ `.الردود `\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م5"))
@bot.on(sudo_cmd("م5", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n\n\n **⌔╎قائـمه اوامـر الرفـع :**\n⪼ `.رفع تاج ` \n⪼ `.رفع بقلبي ` \n⪼ `.رفع بكلبي ` \n⪼ `.رفع مرتبط ` \n⪼ `.رفع مرتبطه ` \n⪼ `.رفع حبيبي ` \n⪼ `.رفع مرتي ` \n⪼ `.رفع خطيبتي ` \n⪼ `.رفع مزه ` \n⪼ `.رفع صاكه ` \n⪼ `.رفع صاك ` \n⪼ `.رفع ورع ` \n\n⪼ `.رفع جريذي ` \n⪼ `.رفع مطي ` \n⪼ `.رفع حمار ` \n⪼ `.رفع جلب ` \n⪼ `.رفع زباله ` \n⪼ `.رفع فرخ ` \n⪼ `.رفع كواد ` \n\n⪼ `.رفع مدير ` \n⪼ `.رفع منشئ ` \n⪼ `.رفع مطور ` \n\n\n **⌔╎قائـمه اوامـر النسـب :**\n⪼ `.نسبه الحب ` \n⪼ `.نسبه النجاح ` \n⪼ `.نسبه الانوثه ` \n⪼ `.نسبه الرجوله ` \n⪼ `.نسبه الكراهيه ` \n⪼ `.نسبه الغباء ` \n⪼ `.نسبه الانحراف `\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م6"))
@bot.on(sudo_cmd("م6", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الحمايه قفل/فتح :** \n⪼ `.الكل ` \n⪼ `.الدردشه ` \n⪼ `.الوسائط `\n⪼ `.الملصقات ` \n⪼ `.المتحركه ` \n⪼ `.الاضافه `\n⪼ `.الاونلاين `\n⪼ `.الماركدون `\n⪼ `.الالعاب `\n⪼ `.التثبيت `\n⪼ `.المعلومات `\n⪼ `.الاعدادات ` لرؤية الاعدادات\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م7"))
@bot.on(sudo_cmd("م7", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر التلكراف :** \n⪼ `.تلكراف ميديا ` \n⪼ `.تلكراف نص ` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م8"))
@bot.on(sudo_cmd("م8", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الملصقات :** \n⪼ `.ملصق ` \n⪼ `.معلومات الملصق ` \n⪼ `.حزمه ` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م9"))
@bot.on(sudo_cmd("م9", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر التاك :** \n⪼ `.تاك ` \n⪼ `.للكل ` + الكلام \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م10"))
@bot.on(sudo_cmd("م10", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الكشف :** \n⪼ `.الايدي ` \n⪼ `.ايدي ` \n⪼ `.رابط الحساب ` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########### for SOURCE Ralls by ~ @QQ070 ###########


import random

from telethon import events

@bot.on(admin_cmd("م11"))
@bot.on(sudo_cmd("م11", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝙂𝙍𝙊𝙐𝙋](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر المجموعه :** \n⪼ `.الرابط ` \n⪼ `.رسائلي ` \n⪼ `.غادر ` \n⪼ `.محادثه صوتيه ` \n⪼ `.دعوه للمكالمه ` \n⪼ `.رفع مشرف ` \n⪼ `.تنزيل مشرف ` \n⪼ `.رفع مالك ` \n\n**⌔╎اوامـر حمايـة المجموعـه :** \n⪼ `.تفعيل حمايه المجموعه ` \n⪼ `.تعطيل حمايه المجموعه ` \n⪼ `.الاعدادات ` \n\n**⌔╎اوامـر  التـاك :**\n⪼ `.تاك 10 ` \n⪼ `.تاك 50 ` \n⪼ `.تاك 100 ` \n⪼ `.تاك 150 ` \n⪼ `.تاك 200 ` \n⪼ `.تاك 300 ` \n⪼ `.تاك 500 ` \n⪼ `.تاك 1k ` \n⪼ `.معرفات 100 ` \n⪼ `.معرفات 200 ` \n⪼ `.معرفات 300 ` \n\n**⌔╎اوامـر  الكشـف والاحصائيـات :** \n⪼ `.الاحصائيات ` \n⪼ `.معلومات ` \n⪼ `.المجموعه ` \n⪼ `.المشرفين ` \n⪼ `.الاعضاء ` \n⪼ `.البوتات ` \n⪼ `.الحسابات المحذوفه ` \n⪼ `.تنظيف الحسابات المحذوفه` \n⪼ `.مسح المحظورين ` \n⪼ `.معلومات تخزين المجموعه ` \n⪼ `.تغير صوره المجموعه ` \n\n**⌔╎اوامـر اضـافة وسحـب الاعضـاء وتفلـيش المجموعـات :** \n⪼ `.ضيف + رابط المجموعه ` \n⪼ `.تفليش ` \n**- ملاحظـه هامـه :**\nلا تستخـدم هذان الامـران بكثـره او بحسـابك الرسمـي .. قد يؤدي غالبـاً الى حظـر وحذف حسـابك من الشـركه .. استخـدم حسـاب وهمي منصـب\n\n𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م12"))
@bot.on(sudo_cmd("م12", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الترجـمه :**\n\n `.ترجمه ar`  بالرد على الرسالـه\n**•❒ ترجمـة النص المـحدد من أي لغـه الى اللغـه العربيـه**\n\n `.ترجمه en`  بالرد على الرسالـه\n**•❒ ترجمـة النص المـحدد من أي لغـه الى اللغـه الانجليزيـه**\n\n `.صوت كوكل en/ar`  بالرد على الرسالـه\n**•❒ ترجمـة النص المـحدد الى جمله صوتيـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م13"))
@bot.on(sudo_cmd("م13", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الاغـاني والبحث :** \n\n❶** يـوتيـوب :**\n\n `.بحث` + اسـم\n**•❒ لتحميل الاغانـي من يوتيوب بدقـه عاليـه 360**\n`.اغنيه` + اسـم\n**•❒ لتحميل الاغانـي من يوتيوب ميـوزك بسـرعـه فائقـه**\n `.فيديو` + اسـم\n**•❒ لتحميل مقاطـع الفيديـو من يوتيوب**\n `.يوتيوب` + كلمـه\n**•❒ للبحث عن روابـط بالكلـمه المعطـاه على يوتيوب**\n `.تحميل ف` + رابـط\n**•❒ لتحميل مقاطـع الفيديو من اليوتيوب عن طريق الرابـط**\n `.تحميل ص` + رابـط\n**•❒ لتحميل مقاطـع الصوت من يوتيوب عن طريق الرابـط**\n\n\n❷** انستجـرام :**\n\n `.انستا` + رابـط\n**•❒ للتحميل من الانستكرام**\n\n\n❸** تيـك تـوك :**\n\n `.تيكتوك` بالـرد علـى رابـط\n**•❒ لتحميل مقاطـع الفيديـو من تيـك تـوك**\n\n\n\❹** لايكـي :**\n\n `.لايكي` بالـرد علـى رابـط\n**•❒ لتحميل مقاطـع الفيديـو من التطبيـق الشهيـر لايكـي**n\n\n❺** فيس بـوك :** \n\n`.فيسبوك` + رابط\n**•❒ لتحميل الفيديو من فيس بوك**\n`.فيس` بالرد ع الرابط\n**•❒ لتحميل الفيديو من فيس بوك بالـرد ع الرابـط**\n\n\n❻** تـويتـر :** \n\n`.تويتر` + رابط\n**•❒ لتحميل الفيديو من تويتـر**\n`.تويت` بالرد ع الرابط\n**•❒ لتحميل الفيديو من تـويتـر بالـرد علـى رابـط**\n\n\n❼** بنتـرسـت :** \n\n`.ترست` + رابط\n**•❒ لتحميل مقاطـع الفيديو والصـور من بنتـرسـت**\n\n\n❽** سنـاب شـات :** \n\n`.سناب` + رابط\n**•❒ لتحميل مقاطـع الفيديو من سنـاب شـات**\n\n\n❾** جـوجـل :**\n\n `.جوجل` + كلمـه\n**•❒ للبحث عـن الكلمـه في محرك البحث جـوجل**\n `.صور` + كلمـه / `.صور` + عدد + كلمـه\n**•❒ لتحميل الصـور من محرك البحث جـوجل**\n `.متحركه` + كلمـه\n**•❒ لتحميل متحركـات عبـر البحـث بالكـلمه**\n `.تحليل` بالرد على صوره\n**•❒ للبحث عن مصادر الصوره الاصليه وشبيهاتها على جـوجل**\n `.تخمين`  بالرد على ملصق\n**•❒ للبحث على مصادر الصورة الاصليه على جـوجل**\n\n\n❿** متجـر جوجـل بـلاي :**\n\n `.متجر` + اسـم التطبيـق\n**•❒ لـ البحث عن تفاصيـل وروابـط التطبيقـات والالعـاب علـى جوجـل بـلاي .. الامـر يدعـم اللغـه العربيـه**\n `.تطبيق` + اسـم التطبيـق\n**•❒ لـ تحميـل التطبيقـات والالعـاب غير محدود وبأحجـام كبيـره تصـل الى 2 جيجـا بايت .. قـم بكتابـة الاسـم بالانجلـش بطـريقـه صحيحـه او قم اولاً باستخـدام الامر .متجر + اسم التطبيق بالعربي للحصول ع اسم التطبيق بالانجلـش ..**\n\n\n⓫** بحـث الافـلام :**\n\n `.فلم` + اسـم الفلـم\n**•❒ لـ تحميـل الافـلام الاجنبيـه بدقـه عاليـه ✓..**\n\n\n⓬** بحث كتـب وروايـات :**\n\n `.رواية`/`.كتاب` + اسـم الروايـة او الكتـاب\n**•❒ لـ تحميـل الكتـب والروايـات ✓..**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########### for SOURCE Ralls by ~ @QQ070 ###########


import random

from telethon import events


@bot.on(admin_cmd("م14"))
@bot.on(sudo_cmd("م14", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الانتحال :** \n⪼ `.نسخ`  \n⪼ `.اعاده` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م15"))
@bot.on(sudo_cmd("م15", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر النت :** \n⪼ `.بنك`  \n⪼ `.سرعه النت` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م16"))
@bot.on(sudo_cmd("م16", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر البوت :** \n⪼ `.اعاده تشغيل`  \n⪼ `.ايقاف ` \n⪼ `.تحديث ` \n⪼ `.تحديث الان `\n\n\n**⌔╎قائـمه اوامر بـوت فـاذر للبـوت المسـاعد :** \n⪼ `.تعيين اسم البوت`  \n⪼ `.تعيين صورة البوت ` \n⪼ `.تعيين نبذة البوت ` \n⪼ `.تعيين وصف البوت ` \n\n⪼ `.انلاين تفعيل ` \n⪼ `.انلاين تعطيل `\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################

import random

from telethon import events


@bot.on(admin_cmd("م17"))
@bot.on(sudo_cmd("م17", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الحساب :** \n⪼ `.ضع اسم` لتغير اسم حسابك \n⪼ `.جلب صوره` لتغير صوره حسابك \n⪼ `.ضع معرف ` لتغير معرف حسابك \n⪼ `.ضع بايو ` لتغير بايو حسابك \n⪼ `.كروباتي ` لعرض المجموعات التي انشأتها \n⪼ `.تهيئه الكل ` لحذف جميع صور حسابك \n⪼ `.تهيئه ` لحذف صوره واحده من حسابك \n⪼ `.الحساب ` لعرض معلومات الحساب \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########### for SOURCE Ralls by ~ @QQ070 ###########


import random

from telethon import events


@bot.on(admin_cmd("م18"))
@bot.on(sudo_cmd("م18", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر السورس :** \n⪼ `.السورس ` لعرض معلومات السورس \n⪼ `.المطور` \n⪼ `.المده ` لعرض مدة استخدام السورس \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م25"))
@bot.on(sudo_cmd("م25", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n**⌔╎قائمـه الوقتـي :**\n\n`.اسم وقتي` \n**⇚ لوضع وقت يتغير مع اسم حسابك كل دقيقـه بالزخـرفـه العـامه 𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬 **\n\n`.البروفايل الوقتي` \n**⇚ لوضع وقت يتغير مع صورة حسابك كل دقيقـه .. تابـع الشـرح اولاً https://t.me/Repthon_vars/13 هنـا**\n\n`.بايو وقتي` \n**⇚ لوضع وقت يتغير مع بايو حسابك كل دقيقـه .. تابـع الشـرح اولاً https://t.me/Repthon_vars/13 هنـا**\n\n`.انهاء + نفس الامر` \n**⇚ لانهـاء اوامـر الوقتـي**\n\n\n\**⇚ لوضع شعـار او رمـز بجانب الاسـم الوقتـي الشـرح : https://t.me/Repthon_vars/13 هنـا**n\n\n**⌔╎اعـداد فـارات الوقتـي المزغـرفـه :**\n\n`.ضع فار BA_FN ١٢٣٤٥٦٧٨٩٠` وانتظر دقيقـه ودز امـر `.الاسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام العربيـه ١٢٣٤٥٦٧٨٩٠**\n\n`.ضع فار BA_FN 𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الـزخرفـة بالارقـام  𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎**\n\n`.ضع فار BA_FN ₁₂₃₄₅₆₇₈₉₀` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  ₁₂₃₄₅₆₇₈₉₀**\n\n`.ضع فار BA_FN ¹²³⁴⁵⁶⁷⁸⁹⁰` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  ¹²³⁴⁵⁶⁷⁸⁹⁰**\n\n`.ضع فار BA_FN ➊➋➌➍➎➏➐➑➒✪` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  ➊➋➌➍➎➏➐➑➒✪**\n\n`.ضع فار BA_FN ❶❷❸❹❺❻❼❽❾⓿` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  ❶❷❸❹❺❻❼❽❾⓿**\n\n`.ضع فار BA_FN ➀➁➂➃➄➅➆➇➈⊙` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  ➀➁➂➃➄➅➆➇➈⊙**\n\n`.ضع فار BA_FN ⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  ⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪**\n\n`.ضع فار BA_FN ①②③④⑤⑥⑦⑧⑨⓪` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  ①②③④⑤⑥⑦⑧⑨⓪**\n\n`.ضع فار BA_FN 𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢**\n\n`.ضع فار BA_FN 𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶**\n\n`.ضع فار BA_FN 𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘**\n\n`.ضع فار BA_FN １２３４５６７８９０` وانتظر دقيقـه ودز امـر `.اسم وقتي`\n**⇚ لـ الزخرفـة بالارقـام  １２３４５６７８９０**\n\n`.انهاء الاسم الوقتي` / `.انهاء البايو الوقتي` \n**⇚ لانهـاء اوامـر الوقتـي المزخرفـه**\n\n\n**- ملاحظـه هـامـه ⚠️ :**\n احنا جمعنـا لكـم كل زخـارف الارقـام الموجودة ع التلي + تقـدر تضيـف اي زخـارف للارقـام عبـر الامـر .ضع فار BA_FN + سلسلة الارقـام التريدهـا \n\n\n𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م26"))
@bot.on(sudo_cmd("م26", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑩𝑳𝑨𝑪𝑲𝑳𝑰𝑺𝑻](t.me/Repthon) 𓆪\n **⌔╎القائمة السوداء :** \n⪼ `.منع كلمه + الكلمه ` لمنع كلمه  \n⪼ `.الغاء منع + الكلمه` \n⪼ `.الكلمات المحظوره` \n⪼ `.ازعاج` \n⪼ `.الغاء ازعاج` \n⪼ `.قائمة الازعاج` \n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Rallsthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م27"))
@bot.on(sudo_cmd("م27", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائمـه التحويلات :** \n\n**❶ تحـويلات :** \n⪼ `.لصوره ` بالـرد ع ملصق  \n⪼ `.لملصق`  بالـرد ع صـوره\n⪼ `.لمتحرك` بالـرد ع ملصق متحرك \n⪼ `.حول بصمه` \n⪼ `.حول صوت` \n\n\n**❷ تحـويلات :** \n⪼ `.دائري ` بالرد ع ملصق او صـوره \n⪼ `.لمتحركه`  بالـرد ع صـوره او ملصـق لتحـويلها ⇄ متحـركـه جاهـزه\n⪼ `.متحرك` بالرد ع فيديـو لتحـويله ⇄ متحـركـه \n⪼ `.نوت` بالـرد ع فيديـو لتحـويله ⇄ فيديـو نـوت \n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م28"))
@bot.on(sudo_cmd("م28", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎قائـمه اوامر الکـشف العـام :** \n\n `.الاسماء` بالرد/المعرف/الايدي\n**•❒ لعرض قائمـه بسجل جميع اسماء الحساب + تاريخ انضمـام  الشخص على تليكـرام .**\n\n `.كروباتي عام/مالك/مشرف` \n**•❒ عام ⇎ قائمـه بجميع الكروبات المتواجد بيها**\n**•❒ مالك ⇎ قائمـه بجميع كروباتك الملكـيه**\n**•❒ مشرف ⇎ قائمـه بجميع الكروبات الانته مشرف بيها**\n\n `.قنواتي عام/مالك/مشرف` \n**•❒ عام ⇎ قائمـه بجميـع القنوات المنضـم بيها**\n**•❒ مالك ⇎ قائمـه بجميـع قنـواتك الملكـيه**\n**•❒ مشرف ⇎ قائمـه بجميـع القنوات الانته مشـرف بيها**\n\n `.احصائياتي/احصائياته` \n**•❒ لعرض قائمـه بجميـع احصائيات حسابك على تلكـرام**\n\n `.المشرفين` / .المشرفين + معـرف الكروب/القنـاة\n**•❒ لعـرض قائمـه بجميع مشرفين المجموعه/القناة المحدده**\n\n `.البوتات` / .البوتات + معـرف الكروب\n**•❒ لعـرض قائمـه بجميع بوتات المجموعه المحدده**\n\n `.الاعضاء` / .الاعضاء + معرف الكروب\n**•❒ لعـرض قائمـه بجميـع اعضـاء المجموعة المحدده**\n\n `.المجموعه` / .المجموعه + معرف الكروب/القناه\n**•❒ لرؤيـة كل المعلومات المتعلقه بالمجموعه او القناة المحدده**\n\n `.اكسباير` \n**•❒ لعـرض لستـة معلومات خاصه بالمجموعه او القناة المحدده**\n\n `.مسح المحظورين` \n**•❒ مسـح كل المحظورين في الدردشـه المحدده**\n\n `.تنظيف الحسابات` \n**•❒ لتنظـيف المجموعـه او القناة المحدده من الحسابات المحذوفـه**\n\n `.الاحصائيات` \n**•❒ لعـرض قائمـه بالحسابات المتصله والآخـر ظهور والحسابات المحذوفـه الـخ ...**\n\n 𓆩 [𝙎𝙊𝙐𝙍??𝞝 𝐑𝐀𝐈𝐈𝐒](t.me/RallsThon) 𓆪")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("م29"))
@bot.on(sudo_cmd("م29", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n **⌔╎اوامـر الميديـا ( صـورة - فيديـو ) ذاتيـة التدمير :** \n\n⪼ `.ذاتيه ` بالرد ع (صوره / فيديو) ذاتيـة التدمير لحفظها بـ حافظـة حسابك   \n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

import random

from telethon import events


@bot.on(admin_cmd("م32"))
@bot.on(sudo_cmd("م32", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n\n**⌔╎اوامــر تجميع نقاط🎆♥️ **\n\n**- لتجميع النقاط قم بكتابة الامر الاتي `.تجميع نقاط`** \n\n\n**⌔╎اوامر الصيد🧸❤️ :**\n⪼ لمعرفة اوامر الصيد قم بكتابة الامر الاتي `.الصيد` \n\n\n𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

import random

from telethon import events


@bot.on(admin_cmd("م33"))
@bot.on(sudo_cmd("م33", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n\n**⌔╎أوامـر حــمــايــة الــخــاص🔕♥️ **\n\n**- لتفعيل حماية الخاص قم بكتابة الامر الاتي `.الحمايه تفعيل`** \n\n\n**⌔╎اوامر إطفاء حماية الخاص🧸❤️ :**\n⪼ **لأطفاء حماية الخاص قم بكتابة الامر الاتي `.الحمايه تعطيل`** **\n\n\n𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪")

import random

from telethon import events


@bot.on(admin_cmd("قائمه"))
@bot.on(sudo_cmd("قائمه", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺](t.me/Repthon) 𓆪\n⪼ **قائمه اوامر ريبـــثون قم بضغط على الامر لنسخه :**\n⪼ `.ترحيب` \n⪼ `.مسح ترحيب` \n⪼ `.الترحيب ` \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.المحظورين` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.رفع` - مطي ، جلب \n⪼ `.تثبيت` \n⪼ `.الغاء تثبيت` \n⪼ `.الغاء تثبيت الكل` \n⪼ `.منع كلمه` \n⪼ `.الغاء منع` \n⪼ `.رفع مشرف` \n⪼ `.رفع مالك` \n⪼ `.تنظيف`  》》 يستخدم بالرد على الرساله \n⪼ `.نسخ`  》》لنسخ بروفايل الشخص \n⪼ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ \n⪼ `نسبه الانوثه` \n⪼ `.اعادة التشغيل` \n⪼ `.ايقاف التشغيل` \n⪼ `.تحديث`  》 لتحديث السورس \n⪼ `.بحث` 》 مثلا  `.بحث عشك` \n⪼ `.صوره` 》 مثلا  .صوره طياره \n⪼ `.ايدي` 》 لعرض معلومات البوت \n⪼ `.بنك`  》 يعرض البنك \n⪼ `.سرعه النت` 》 قياس سرعه النت \n⪼ `.ترجمه ar` \n⪼ `.ترجمه en`  \n⪼ `.تكرار`+الرقم + الكلمه \n⪼ `.سبام`  》 كذالك نفس التكرار \n⪼ `.سماح` 》الامر فقط لميزه  حمايه الخاص \n⪼ `.رفض` 》 كذالك \n⪼ `.الكل` 》 لرفض الكل وتشغيل الحمايه \n⪼ `.بلوك` 》 من الخاص \n⪼ `.انبلوك` 》》لرفع الحظر من الخاص  \n⪼ `.المسموح لهم` 》لعرض قائمه السماح \n⪼ `.ايدي` 》 لعرض معلومات المستخدم \n⪼ `.الايدي` \n⪼ `.المجموعه 》》لعرض معلومات المجموعه ` \n⪼ `.السورس 》》 لعرض معلومات السورس ` \n⪼ `.مغادره` 》 تستخدم  لمغادره الكروب \n⪼ `.تاك` 》 لعمل تاك للكل \n⪼ `.للكل` + الكلام 》 لعمل تاك \n⪼ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره \n⪼ `.تلكراف نص` 》 بالرد على الكتابه\n⪼ `.المطور` \n 𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻](t.me/Repthon) 𓆪 ")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon import events


@bot.on(admin_cmd("المطور"))
@bot.on(sudo_cmd("المطور", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹](t.me/Repthon) 🧸♥️𓆪\n**𓍹━─━─━─━─━𝗥𝗲𝗽─━─━─━─━𓍻**\n **𓄂**╺  𝑫𝑬𝑽 ❶╰──► @E_7_V ༗\n\n **𓄂**╺  𝑫𝑬𝑽 ❷╰──► @ul4ul ༗")

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################

import random

from telethon import events


@bot.on(admin_cmd("رابط الحذف"))
@bot.on(sudo_cmd("رابط الحذف", allow_sudo=True))
async def _(Ralls):
    await eor(Ralls, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - 𝘿𝙀𝙇𝙀𝙏𝙀](t.me/Repthon) 🗑♻️𓆪\n**𓍹━─━─━─━─𝗥𝗲𝗽─━─━─━─━𓍻**\n\n **✵│رابـط الحـذف ↬** https://telegram.org/deactivate \n\n\n **✵│بـوت الحـذف  ↬** @LC6BOT ")

########################  SOURCE Repthon ~ BY: QQ070 (@QQ070)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جلب(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جلب(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{custom}](tg://user?id={user.id}) \n ⌔∮تم رفعه جلب في ريس",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{tag}](tg://user?id={user.id}) \n ⌔∮تم رفعه جلب في ريس",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مرتي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مرتي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{custom}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{tag}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )


########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع تاج(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع تاج(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{custom}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه تـاج 👑🔥 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{tag}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه تـاج 👑🔥 ",
        )


########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع بكلبي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع بكلبي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{custom}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه بڪلبك 🖤 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{tag}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه بڪلبك 🖤 ",
        )


########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع بقلبي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع بقلبي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"**⌔╎المستخدم** [{custom}](tg://user?id={user.id}) \n **⌔╎تـم رفعـه بــ قلبـك .. نبـض ووريـد 🖤** ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"**⌔╎المستخدم** [{custom}](tg://user?id={user.id}) \n **⌔╎تـم رفعـه بــ قلبـك .. نبـض ووريـد 🖤** ",
        )


########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جريذي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جريذي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{custom}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{tag}](tg://user?id={user.id}) \n ⌔╎تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )


########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع فرخ(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع فرخ(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """ For .link command, generates a link to the user's PM with a custom text. """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{custom}](tg://user?id={user.id}) \n ⌔╎تم رفعه فرخ هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔╎المستخدم [{tag}](tg://user?id={user.id}) \n ⌔╎تم رفعه فرخ هنا ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################

mth = [
    "100% تحبك وتخاف عليك",
    "100% يحبج ويخاف عليج",
    "91% جـزء من قـلبه 💞",
    "81% تموت عليك ههاي ",
    "81% يموت عليج ههذا ",
    "40% واحد حيوان ومصلحه عوفه ",
    "50% شوف شعندك وياه ",
    "30% خاين نصحيا عوفيه ميفيدج ",
    "25% مصادق غيرج ويكلج احبج",
    "25% واحد كلب ابن كلب عوفه",
    "0% يكهرك ",
    "0% تكرهك ",
]

zid = [
    "100%",
    "99%",
    "98%",
    "97%",
    "96%",
    "95%",
    "90%",
    "89%",
    "88%",
    "87%",
    "86%",
    "85%",
    "80%",
    "79%",
    "78%",
    "77%",
    "76%",
    "75%",
    "70%",
    "69%",
    "68%",
    "67%",
    "66%",
    "65%",
    "60%",
    "59%",
    "58%",
    "57%",
    "56%",
    "55%",
    "50%",
    "48%",
    "47%",
    "46%",
    "45%",
    "40%",
    "39%",
    "38%",
    "37%",
    "36%",
    "35%",
    "30%",
    "29%",
    "28%",
    "27%",
    "25%",
    "20%",
    "19%",
    "18%",
    "17%",
    "16%",
    "15%",
    "10%",
    "9%",
    "8%",
    "7%",
    "6%",
    "5%",
    "4%",
    "3%",
    "2%",
    "1%",
    "0%",

]

@bot.on(admin_cmd(pattern="نسبه الحب(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallst = random.choice(mth)
    await edit_or_reply(mention, f"⌔╎نـسـبتكم انـت و [{Rallsth}](tg://user?id={user.id}) هـي {Rallst} 😔🖤")
@bot.on(admin_cmd(pattern="نسبه الانوثه(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallst = random.choice(zid)
    await edit_or_reply(mention, f"⌔╎نسبه الانوثه لـ [{Rallsth}](tg://user?id={user.id}) هـي {Rallst} 🤰")
@bot.on(admin_cmd(pattern="نسبه الغباء(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallst = random.choice(zid)
    await edit_or_reply(mention, f"⌔╎نسبه الغباء لـ [{Rallsth}](tg://user?id={user.id}) هـي {Rallst} 😂💔")
@bot.on(admin_cmd(pattern="نسبه الانحراف(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallst = random.choice(zid)
    await edit_or_reply(mention, f"⌔╎نسبة الانحراف لـ [{Rallsth}](tg://user?id={user.id}) هـي {Rallst} 🥵🖤")
@bot.on(admin_cmd(pattern="نسبه المثليه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallst = random.choice(zid)
    await edit_or_reply(mention, f"⌔╎نسبه المثليه لـ [{Rallsth}](tg://user?id={user.id}) هـي {Rallst} 🤡 🏳️‍🌈.")
@bot.on(admin_cmd(pattern="نسبه النجاح(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallst = random.choice(zid)
    await edit_or_reply(mention, f"⌔╎نسبه النجاح لـ [{Rallsth}](tg://user?id={user.id}) هـي {Rallst} 🤓.") 
@bot.on(admin_cmd(pattern="نسبه الكراهيه(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallst = random.choice(zid)
    await edit_or_reply(mention, f"⌔╎نسبه الكراهـي لـ [{Rallsth}](tg://user?id={user.id}) هـي {Rallst} 🤮.")

@bot.on(admin_cmd(pattern="رفع ورع(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه ورع القـروب .. بنجـاح😹🙇🏻.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع مزه(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخدمه ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـها مـزة الكروب .. بنجـاح 🥳💃.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مطي سبورتي 🐴.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع حمار(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حمار جحا 😂🐴.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع زباله(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه زباله معفنه 🗑.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه منشئ الكروب 👷‍♂️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع مدير(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه مدير الكروب 🤵‍♂️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع كواد(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه كـواد .. بنجـاح 👀. ** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع مرتبط(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـه مرتبـط .. بنجـاح 💍💞** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع مرتبطه(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخدمه ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تـم رفعـهـا مرتبطـه .. بنجـاح 💍💞. .** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع حبيبي(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـه حبيبـج .. بنجـاح 💍🤵‍♂👰🏻‍♀.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع خطيبتي(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚺 ╎ المستخدمه ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎ تم رفعـهـا خطيبتك .. بنجـاح 💍👰🏼‍♀️.** \n**🤵‍♂️ ╎ بواسطـه  :** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـه صاك 🤴 .** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
@bot.on(admin_cmd(pattern="رفع صاكه(?:\s|$)([\s\S]*)"))
async def Ralls(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**🚹 ╎ المستخدم ⪼ • ** [{Rallsth2}](tg://user?id={user.id}) \n☑️ **╎  تم رفعـها صاكه 👸🏼.** \n**🤵‍♂️ ╎ بواسطـه  : ** {my_mention} ")
########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import random

from telethon.tl.types import MessageEntityMentionName

ppp = [
    "100% 🔱💕.",
    "90%",
    "80%",
    "70%",
    "60%",
    "50%",
    "40%",
    "30%",
    "20%",
    "10%",
    "0%",
]


@bot.on(admin_cmd(pattern="نسبه الانوثه(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="نسبه الانوثه(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    ioi = random.choice(ppp)
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔╎نسبه الانوثه لـ [{custom}](tg://user?id={user.id}) هـي {ioi} ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔╎نسبه الانوثه لـ [{tag}](tg://user?id={user.id}) هـي {ioi} ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  SOURCE Ralls ~ BY: QQ070 (@QQ070)  ########################


import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "Repthon"
CAT_IMG = "userbot/extras/Repthon_1.jpg"
CUSTOM_ALIVE_TEXT = "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑫𝑬𝑽𝑳𝑶𝑷𝑬𝑹 𓆪"
EMOJI = "𓄂†"


@bot.on(admin_cmd(outgoing=True, pattern="$مطور"))
@bot.on(sudo_cmd(pattern="$مطور", allow_sudo=True))
async def dev(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗥𝗲𝗽ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 1 ↬ @E_7_V ༗\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 2 ↬ @ul4ul ༗\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗥𝗲𝗽ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗥𝗲𝗽ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 1 ↬ @E_7_V ༗\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 2 ↬ @ul4ul ༗\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ𝗥𝗲𝗽ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻",
        )
