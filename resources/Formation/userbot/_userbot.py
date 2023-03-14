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

    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_IDill verify the both loggers group
async def verifyLoggerGroup():

    """

    التاكد من كروب التخزين

    """

    flag = False

    if BOTLOG:

        try:

            entity = await bot.get_entity(BOTLOG_CHATID)

            if not isinstance(entity, types.User) and not entity.creator:

                if entity.default_banned_rights.send_messages:

                    LOGS.info(

                        "لا توجد صلاحيات كافية لارسال الرسائل في كروب الحفظ او التخزين"

                    )

                if entity.default_banned_rights.invite_users:

                    LOGS.info(

                        "لا توجد صلاحيات كافية لاضافة الاعضاء في كروب الحفظ او التخزين"

                    )

        except ValueError:

            LOGS.error("لم يتم التعرف على فار كروب الحفظ")

        except TypeError:

            LOGS.error("يبدو انك وضعت فار كروب الحفظ بشكل غير صحيح")

        except Exception as e:

            LOGS.error("هنالك خطا ما للتعرف على فار كروب الحفظ\n" + str(e))

    else:

        descript = "⪼ هذه هي مجموعه الحفظ الخاصه بك لا تحذفها ابدا  𓆰."

        photobt = await bot.upload_file(file="userbot/extras/Repthon1.jpg")

        _, groupid = await create_supergroup(

            "مــجــمــوعــة اشــعــارات ريبـــثون", bot, Config.BOT_USERNAME, descript, photobt

        )

        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)

        print("تم انشاء كروب الحفظ بنجاح")

        flag = True

    if PM_LOGGER_GROUP_ID != -100:

        try:

            entity = await jmub.get_entity(PM_LOGGER_GROUP_ID)

            if not isinstance(entity, types.User) and not entity.creator:

                if entity.default_banned_rights.send_messages:

                    LOGS.info("لا توجد صلاحيات كافية لارسال الرسائل في كروب التخزين")

                if entity.default_banned_rights.invite_users:

                    LOGS.info("لا توجد صلاحيات كافية لاضافة الاعضاء في كروب التخزين")

        except ValueError:

            LOGS.error(

                "لم يتم العثور على ايدي كروب التخزين تاكد من انه مكتوب بشكل صحيح "

            )

        except TypeError:

            LOGS.error("صيغه ايدي كروب التخزين غير صالحة.تاكد من انه مكتوب بشكل صحيح ")

        except Exception as e:

            LOGS.error("حدث خطأ اثناء التعرف على كروب التخزين\n" + str(e))

    else:

        descript = "❃ لا تحذف او تغادر المجموعه وظيفتها حفظ رسائل التي تأتي على الخاص"

        photobt = await bot.upload_file(file="userbot/extras/Repthon2.jpg")

        _, groupid = await create_supergroup(

            "مجموعة التخزين", bot, Config.BOT_USERNAME
          )

        addgvar("PM_LOGGER_GROUP_ID", groupid)

        print("تم عمل الكروب التخزين بنجاح واضافة الفارات اليه.")

        flag = True

    if flag:

        executable = sys.executable.replace(" ", "\\ ")

        args = [executable, "-m", "userbot"]

        os.execle(executable, *args, os.environ)

        sys.exit(0)
