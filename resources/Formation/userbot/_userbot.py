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
usr = "𝚁𝚎𝚙𝚝𝚑𝚘𝚗 USERBOT -{}".format(Tlk)
adn = "𝚁𝚎𝚙𝚝𝚑𝚘𝚗 ADMIN TOOLS -{}".format(Tlk)
ani = "𝚁𝚎𝚙𝚝𝚑𝚘𝚗 ANIMATIONS -{}".format(Tlk)
tsh = "𝚁𝚎𝚙𝚝𝚑𝚘𝚗 TOSHA -{}".format(Tlk)
ast = "𝚁𝚎𝚙𝚝𝚑𝚘𝚗 ASSISTANT -{}".format(Tlk)
pmt = "𝚁𝚎𝚙𝚝𝚑𝚘𝚗 ASSISTANT PM -{}".format(Tlk)

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
