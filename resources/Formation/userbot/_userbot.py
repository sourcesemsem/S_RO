# Hey There

import os
import sys
import time
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger

import heroku3
from dotenv import load_dotenv
from pySmartDL import SmartDL
from pytgcalls import PyTgCalls
from requests import get
from telethon import TelegramClient 
from telethon.sessions import StringSession 

from userbot.Config import Config
from userbot.tosh import Tlk

StartTime = time.time()
icsv = "1.0.0"

ICS_ID = ["5502537272"]

# for print :
usr = "REPTHON USERBOT -{}".format(Tlk)
adn = "REPTHON ADMIN TOOLS -{}".format(Tlk)
ani = "REPTHON ANIMATIONS -{}".format(Tlk)
tsh = "REPTHON TOSHA -{}".format(Tlk)
ast = "REPTHON ASSISTANT -{}".format(Tlk)
pmt = "REPTHON ASSISTANT PM -{}".format(Tlk)

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="[%(asctime)s]- %(name)s- %(levelname)s- %(message)s",
        level=INFO,
        datefmt="%m-%d %H:%M:%S",
    )
LOGS = getLogger(__name__)


try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None

# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

# Variables

BOTLOG = Config.BOTLOG

BOTLOG_CHATID = Config.BOTLOG_CHATID

PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID

if Config.SESSION:
    session_name = str(Config.SESSION)
    try:
        if session_name.endswith("="):
            bot = TelegramClient(
                StringSession(session_name), Config.API_ID, Config.API_HASH
            )
        else:
            bot = TelegramClient(
                "BOT_TOKEN", api_id=Config.API_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.SESSION)
        call_py = PyTgCalls(bot)
    except Exception as e:
        LOGS.warn(f"SESSION - {str(e)}")
        sys.exit()
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Config.API_ID, Config.API_HASH)
    call_py = PyTgCalls(bot)
    
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:

        Config.BOTLOG = False

        Config.BOTLOG_CHATID = "me"

    else:

        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))

        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))

        Config.BOTLOG = True

else:

    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":

        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))

    else:

        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID

    Config.BOTLOG = True

if Config.PM_LOGGER_GROUP_ID == 0:

    if gvarstatus("PM_LOGGER_GROUP_ID") is None:

        Config.PM_LOGGER_GROUP_ID = -100

    else:

        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))

elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":

    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID
async def verifyLoggerGroup():

  """
Will verify the both loggers group
  """

flag = False

if BOTLOG:

     try:

entity = await bot.get_entity(BOTLOG_CHATID)

if not isinstance(entity, types.User) and not entity.creator:

if entity.default_banned_rights.send_messages:

              LOGS.info(

"᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."

                    )

if entity.default_banned_rights.invite_users:

    LOGS.info(

"᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."

                  )

 except ValueError:

LOGS.error("᯽︙تـأكد من فـار المجـموعة  PRIVATE_GROUP_BOT_API_ID.")

 except TypeError:

 LOGS.error(

"᯽︙لا يمكـن العثور على فار المجموعه PRIVATE_GROUP_BOT_API_ID. تأكد من صحتها."

          )

   except Exception as e:

         LOGS.error(

"᯽︙حدث استثناء عند محاولة التحقق من PRIVATE_GROUP_BOT_API_ID.\n"

    + str(e)

          )

  else:

descript = "عزيزي المستخدم هذه هي مجموعه الاشعارات يرجى عدم حذفها - @Repthon"

photobt = await bot.upload_file(file="userbot/extras/Repthon1.jpg")

_, groupid = await create_supergroup(

"مــجــمــوعــة أَشــعــارات ريبـــثون", bot, Config.BOT_USERNAME, descript, photobt

        )

addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)

print("᯽︙تم إنشاء مجموعة المسـاعدة بنجاح وإضافتها إلى المتغيرات.")

flag = True

if PM_LOGGER_GROUP_ID != -100:

        try:

entity = await bot.get_entity(PM_LOGGER_GROUP_ID)

if not isinstance(entity, types.User) and not entity.creator:

if entity.default_banned_rights.send_messages:

        LOGS.info(

"᯽︙الأذونات مفقودة لإرسال رسائل لـ PM_LOGGER_GROUP_ID المحدد."

             )

if entity.default_banned_rights.invite_users:

        LOGS.info(

"᯽︙الأذونات مفقودة للمستخدمين الإضافيين لـ PM_LOGGER_GROUP_ID المحدد."

              )

   except ValueError:

LOGS.error("᯽︙لا يمكن العثور على فار  PM_LOGGER_GROUP_ID. تأكد من صحتها.")

except TypeError:

LOGS.error("᯽︙PM_LOGGER_GROUP_ID غير مدعوم. تأكد من صحتها.")

except Exception as e:

LOGS.error(

"⌯︙حدث استثناء عند محاولة التحقق من PM_LOGGER_GROUP_ID.\n" + str(e)

        )

else:

descript = "᯽︙ وظيفه الكروب يحفظ رسائل الخاص اذا ما تريد الامر احذف الكروب نهائي - @Repthon"

photobt = await bot.upload_file(file="userbot/extras/Repthon2.jpg")

_, groupid = await create_supergroup(

"مجموعة التخزين", bot, Config.BOT_USERNAME, descript, photobt

      )

addgvar("PM_LOGGER_GROUP_ID", groupid)

print("تـم عمـل الكروب التخزين بنـجاح واضافة الـفارات الـيه.")

  flag = True

    if flag:

executable = sys.executable.replace(" ", "\\ ")

args = [executable, "-m", "userbot"]

os.execle(executable, *args, os.environ)

sys.exit(0)
