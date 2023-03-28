#   Rep - THON

from userbot.Config import Config # Ok - 🖤 
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.contacts import UnblockRequest 

USERID = Config.OWNER_ID
Name = Config.ALIVE_NAME
DEFAULTUSER = str(Name) if Name else "Repthon"
mention = f"[{Name}](tg://user?id={USERID})"

Plugin = "userbot/plugins/{}.py"
Admin = "userbot/plugins/Admin/{}.py"
Animation = "userbot/plugins/animations/{}.py"
Tosh = "userbot/plugins/tosha/{}.py"
Assistant = "userbot/plugins/assistant/{}.py"
AssistantPm = "userbot/plugins/assistant/PmTosh/{}.py"

Xtbot = "\"BOT_TOKEN\""
Xt = "BOT_TOKEN"
Xe = "SESSION"

A = Config.API_ID
H = Config.API_HASH
B = Config.BOT_TOKEN
N = Config.NO_LOAD

Start = (
    """
    <------------------------------------>
            يتم تحميل ملفات السورس ريبـــثون
    <------------------------------------>
    """
)

TOSHA = Config.PRIVATE_GROUP_BOT_API_ID
TBOT = Config.BOT_USERNAME
T = Config.COMMAND_HAND_LER or "."
DEVL = "@Repthon"

C = "**⌔╎المعادله ⪼** {}\n  **- الحل ⪼** {}"
Calc = (
    "𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑪𝑨𝑳𝑪𝑼𝑳𝑨𝑻𝑶𝑹 𓆪\n"
    "◐━─━─━─━─**𝗥𝗲𝗽𝘁𝗵𝗼𝗻**─━─━─━─━◐\n"
    "**⌔╎قائـمه اوامر الحاسبه :** \n"
    "⪼ `.حاسبه` + المعادله \n"
    "◐━─━─━─━─**𝗥𝗲𝗽𝘁𝗵𝗼𝗻**─━─━─━─━◐\n"
    "𓆩 𝗦𝗢𝗨𝗥𝗖𝗘 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - [𝘿𝙀𝙑](t.me/E_7_V) 𓆪"
)

kk = [
   "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯",
   "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛"
]

urs = "**⌔╎نسبة نجاحك هيه -** {}"
Fl = [
   "+100% 🔱🖤", "100% 🖤", "95%", "90%","85%", "80%", "75%", "70%", "65%", "60%", "55%", 
   "50%", "45%", "40%", "35%", "30%", "25%", "20%", "15%", "10%", "0%", "-0%"
]

MSGE = (
   f"𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n◐━─━─━─━─**𝗥𝗲𝗽**─━─━─━─━◐\n**⌔╎المستخدم -** {mention}\n**⌔╎البوت - {TBOT}**\n**⌔╎للمساعده - {DEVL}**\n**اكتب {T}بنك لتحقق اذا ما كان البوت يعمل**"
)

Tlk = " تم استرداد ⫸"
IS = "⫷ لايمكن تحميل - {} بسبب {} ⫸"

#- TOSH is the most beautiful girl in the world -#
ICSJ = "<ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ>"
StartLoaded = "<ⵧⵧⵧⵧⵧⵧ⫷ - REPTHON PLUGINS - ⫸ⵧⵧⵧⵧⵧⵧ>"
ASSISTANT = "<ⵧⵧⵧⵧⵧⵧ⫷ - REPTHON ASSISTANT - ⫸ⵧⵧⵧⵧⵧⵧ>"
KIMOTOSHA = "<ⵧⵧⵧⵧⵧⵧⵧⵧ⫷ - REPTHON TOSHA - ⫸ⵧⵧⵧⵧⵧⵧⵧ>"
ANIMATIONS = "<ⵧⵧⵧⵧⵧⵧ⫷ - REPTHON ANIMATIONS - ⫸ⵧⵧⵧⵧⵧ>"
ADMIN = "<ⵧⵧⵧⵧⵧ⫷ - REPTHON ADMIN TOOLS - ⫸ⵧⵧⵧⵧⵧ>"
ASSISTANTPM = "<ⵧⵧⵧⵧⵧ⫷ - REPTHON ASSISTANT PM - ⫸ⵧⵧⵧⵧⵧ>"
ICSW = "<ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ>"
# --- MESSI IS THE BEST PLAYER IN THE WORLD --- #

Plg = "userbot/plugins/*.py"
Adm = "userbot/plugins/Admin/*.py"
Inm = "userbot/plugins/animations/*.py"
Tsh = "userbot/plugins/tosha/*.py"
Ast = "userbot/plugins/assistant/*.py"
Pmt = "userbot/plugins/assistant/PmTosh/*.py"

Message = (
"""       ⫷ تم الانتهاء من التنصيب ⫸
⫷ بوت ريبـــثون يعمل بنجاح الان ⫸
   ⫷ المستخدم: {} - البوت: {} ⫸
   ⫷ ارجع الى حسابك ودز الامر (.الاوامر) ⫸
⫷ @Repthon_support - اذا كنت بحاجه الى مساعده فتوجه الى ⫸
⫷ @E_7_V - تحياتي : روجـــر | بـــاقـــر⫸"""
)

Mesg = [
    '⫷ يتم تحميل انلاين ريبـــثون ⫸',
    '⫷ اكتمل تنزيل انلاين ريبـــثون بدون اخطاء ⫸',
    '⫷ يتم بدء بوت ريبـــثون ⫸',
    '⫷ اكتمل بدء بوت ريبـــثون ⫸'
]

Quotly = [
    '**⌔╎اهلا -** {} **قم برد على الرساله**',
    '**⌔╎اهلا -** {} **التنسيق غير مدعوم**',
    '**⌔╎جاري المعـالجه….**',
    '**⌔╎قم بالرد على الرساله او قم بوضع النص قرب الامر**',
    '**⌔╎اهلا -** {} **خطا في بناء الامر**',
    '**⌔╎يرجى الغاء الحظر من البوت ~** @quotlybot'
]

Cmds = "𓆰 [𝗦𝗢𝗨𝗥𝗖𝗘 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦](t.me/Repthon) 𓆪\n◐━─━─━─━─**𝗥𝗲𝗽**─━─━─━─━◐\n**⌔╎اهلاً بك عزيزي اختر الاوامـر الاتيـه - ملاحظـه : ضع نقطه (.) بداية كل أمر :**\n `.م1`**   ➪ اوامـر الادمن** \n `.م2`**   ➪ اوامـر التسليه**\n `.م3`**   ➪ اوامـر الترحيب**\n `.م4`**   ➪ اوامـر الردود**\n `.م5`**   ➪ اوامـر الرفع**\n `.م6`**   ➪ اوامـر حماية المجموعة**\n `.م7`**   ➪ اوامـر التلكراف**\n `.م8`**   ➪ اوامـر الملصقات**\n `.م9`**   ➪ اوامـر التاك**\n `.م10`** ➪ اوامـر الكشف**\n `.م11`** ➪ اوامـر المجموعه**\n `.م12`** ➪ اوامـر الترجمه**\n `.م13`** ➪ اوامـر البحث**\n `.م14`** ➪ اوامـر الانتحال**\n `.م15`** ➪ اوامـر النت**\n `.م16`** ➪ اوامـر البوت**\n `.م17`** ➪ اوامـر الحساب**\n `.م18`** ➪ اوامـر السورس**\n `.م19`** ➪ اوامـر الزغـرفه**\n `.م20`** ➪ اوامـر المتحركات**\n `.م21`** ➪ اوامـر الهمسه**\n `.م22`** ➪ اوامـر الالعاب**\n `.م23`** ➪ اوامـر الحاسبه**\n `.م24`** ➪ اوامـر هيروكو**\n `.م25`** ➪ اوامـر الوقتـي**\n `.م26`** ➪ اوامـر القائمة السوداء**\n `.م27`** ➪ اوامـر التحـويلات**\n `.م28`** ➪ اوامـر الكـشف العـام**\n `.م29`** ➪ اوامـر ذاتيـة الـتدمير**\n `.م30`** ➪ اوامـر الثيمـات**\n `.م31`** ➪ اوامـر خلفيات الشاشـه**\n `.م32`** ➪ اوامـر الصيد وتجميع النقاط**\n `.م33`** ➪ اوامـر حماية الخاص** ◐━─━─━─━─**𝗥𝗲𝗽**─━─━─━─━◐\n 𓆩 [𝗦𝗢𝗨𝗥𝗖𝗘 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - قنـاة السـورس](t.me/Repthon) 𓆪"

# Help String - Text when u type .help!
HelpString = "𓆩 𝗦𝗢𝗨𝗥𝗖𝗘 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - **قائمـة المساعـده** 𓆪\n◐━─━─━─━─**𝗥𝗲𝗽**─━─━─━─━◐\n**⌔╎اهلا بك عزيزي {} في قائمه الانلاين:**\n\n**⪼ استخدم** `.مساعده واسم الاضافه`\n**لاضهار الاوامر بدون الاستخدام.**\n\n**⪼ استخدم** `.شرح واسم الاضافه`\n**لاضهار الاوامر وطريقه استخدامها وفوائدها**"

# For Dev:
Devt = "𓄂╺  𝑫𝑬𝑽 𝑼𝑺𝑬𝑹\n╰──► {} ༗".format(DEVL)

# For Echo - EchoText:
Echo = [
    '**⌔╎اهلا -** {}\n**⌔╎انه موجود بلفعل في قائمه الازعاج**',
    '**⌔╎هها هلو 🤍🎧 ،**',
    '**⌔╎اهلا -** {} \n**⌔╎قم برد على الرساله لكي تتم اضافته الى قائمه الازعاج**',
    '**⌔╎اهلا -** {} \n**⌔╎تم ايقاف امر الازعاج**',
    '**⌔╎اهلا -** {} \n**⌔╎هذا المستخدم غير مضاف الى قائمه الازعاج**',
    '𓆩 𝗦𝗢𝗨𝗥𝗖𝗘 𝗥𝗲𝗽𝘁𝗵𝗼𝗻 - 𝑬𝑪𝑯𝑶 𝑳𝑰𝑺𝑻 𓆪\n◐━─━─━─━─**𝗥𝗲𝗽**─━─━─━─━◐\n**⌔╎قائمة المضافين للازعاج:**\n',
    '**- ايدي المستخدم :** `{}`\n**- ايدي الـمجموعه :** `{}`\n\n',
    '**⌔╎اهلا - {} \n**⌔╎لم تقم باضافه احد للقائمه**']

# For Join channel
Join = [
await bot(UnblockRequest("@E_7_V"))
await bot(UnblockRequest("@Repthon_bot"))
await bot(JoinChannelRequest("@eighthon"))
await bot(JoinChannelRequest("@Repthon"))      
await bot(JoinChannelRequest("@ZQ_LO"))
await bot(JoinChannelRequest("@Repthon_vars"))
await bot(JoinChannelRequest("@Repthon_cklaish"))
await bot(JoinChannelRequest("@Repthonn"))
await bot(JoinChannelRequest("@Repthon_cc"))
await bot(JoinChannelRequest("@roger21v"))
await bot(JoinChannelRequest("@Repthon_up"))]
