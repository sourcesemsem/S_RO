#RallsThon ®

import asyncio
import random
import pyfiglet
from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError
from time import sleep
from datetime import datetime
from telethon import Button, events
from telethon.events import CallbackQuery
from telethon.utils import get_display_name
from collections import deque
from random import choice
from . import ALIVE_NAME
from ..helpers import fonts as emojify
from ..helpers.utils import reply_id, _icssutils, parse_pre, install_pip, get_user_from_event, _format
from . import deEmojify
from ..helpers import get_user_from_event

M = (
    "┈┈ ╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
    "┈╱╭▏╮╭┻┻╮╭┻┻╮ ╭▏ \n"
    "▕╮╰▏╯┃╭╮┃┃╭╮┃ ╰▏ \n"
    "▕╯┈▏┈┗┻┻┛┗┻┻┻╮ ▏ \n"
    "▕╭╮▏╮┈┈┈┈┏━━━╯ ▏\n"
    "▕╰╯▏╯╰┳┳┳┳┳┳╯ ╭▏ \n"
    "▕┈╭▏╭╮┃┗┛┗┛┃┈ ╰▏ \n"
    "▕┈╰▏╰╯╰━━━━╯┈┈ ▏I'm سبـونـج بــوب\n"
)


@borg.on(admin_cmd(pattern=r"سبونج بوب"))
async def kek(kek):
    await kek.edit(M)

    D = (
        "╭━┳━╭━╭━╮╮\n"
        "┃┈┈┈┣▅╋▅┫┃\n"
        "┃┈┃┈╰━╰━━━━━━╮\n"
        "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
        "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
        "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
        "╲┃┈┈┈┈╭━┳━━━━╯\n"
        "╲┣━━━━━━┫You are كـلبي الــمدلل\n"
    )


@borg.on(admin_cmd(pattern=r"جلبي"))
async def dog(dog):
    await dog.edit(D)
    P = (
        "┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┃┏┗┛┓┃╭┫U   خنـزيـر┃\n"
        "┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
    )


F = (
    "╱▏┈┈┈┈┈┈ ▕╲▕╲┈┈┈\n"
    "▏▏┈┈┈┈┈┈ ▕▏▔▔╲┈┈\n"
    "▏╲┈┈┈┈┈┈╱┈▔┈ ▔ ╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈You are ثعلــب مــاكر\n"
)

E = (
    "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈ν2.ο\n"
)

H = (
    "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈I'm ضــايج\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈So لا تعصــبني\n"
)


@borg.on(admin_cmd(pattern=r"ثعلب"))
async def fox(fox):
    await fox.edit(F)


@borg.on(admin_cmd(pattern=r"فيل"))
async def elephant(elephant):
    await elephant.edit(E)


@borg.on(admin_cmd(pattern=r"معصب"))
async def homer(homer):
    await homer.edit(H)


@borg.on(admin_cmd(pattern=r"خنزير"))
async def pig(pig):
    await pig.edit(P)


A = (
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣷⣄⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⣴⣶⣿⡆⠀⠀⠉⠉⠀⠈⣶⡆⠀\n"
    "⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣷⠀\n"
    "⠀⠀⠀⣼⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄\n"
    "⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷\n"
    "⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⠏\n"
    "⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀\n"
    "⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
)


@borg.on(admin_cmd(pattern=r"مان"))
async def man(man):
    await man.edit(A)
    

C = (
    "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
    "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
    "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
    "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
    "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
    "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
    "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
    "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
    "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
    "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
    "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
)


@borg.on(admin_cmd(pattern=r"صدمه"))
async def sdma(sdma):
    await sdma.edit(C)


N = (
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
    "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
    "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
    "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
    "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
    "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
    "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
    "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)


@borg.on(admin_cmd(pattern=r"نادم"))
async def nadm(nadm):
    await nadm.edit(N)
    

T = (
    "⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿\n"
    "⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿\n"
    "⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿\n"
    "⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿\n"
    "⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿\n"
    "⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿\n"
    "⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿\n"
    "⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿\n"
    "⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹\n"
    "⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄\n"
    "⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀\n"
    "⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘\n"
)


@borg.on(admin_cmd(pattern=r"ترمب"))
async def trmb(trmb):
    await trmb.edit(T)


B = (
    "⠀⠀⠀⠀⢀⣀⣀⣀\n"
    "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
    "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
    "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
    "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
    "⠀\n"
    "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
    "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
    "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
    "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
    "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
    "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
    "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
    "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
)


@borg.on(admin_cmd(pattern=r"همم"))
async def hmm(hmm):
    await hmm.edit(B)


K = (
    "⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
    "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
    "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
    "⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
)


@borg.on(admin_cmd(pattern=r"تشان"))
async def chan(chan):
    await chan.edit(K)


V = (
    "                     ⣤⣶⣶⣶⣦⣤⣄⡀\n⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n⠀⠀⠀⢀⣾⣿⣿⣿⠿⠿⠟⠻⠿⢿⣿⣿⣿⡆\n⠀⠀⠀⢰⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀ ⠈⠉⢻⡇ \n⠀⠀⠀⠈⠿⣿⣇⣠⠤⠤⠤⢤⣀⣤⠤⠤⣺⡏ \n⠀⠀⠀⠀⠐⢉⣯⠹⣀⣀⣢⡸⠉⢏⡄⣀⣯⠁ \n⠀⠀⠀⠀⠡⠀⢹⣆⠀⠀⠀⣀⡀⡰⠀⢠⠖⠂ \n⠀⠀⠀⠀⠀⠈⠙⣿⣿⠀⠠⠚⢋⡁⠀⡜ \n⠀⠀⠀⠀⠀⠀⢸⠈⠙⠦⣤⣀⣤⣤⡼⠁  \n⠀⠀⠀ ⠀⢀⡌⠀⠀⠀⠀ ⠉⢏⡉  \n⠀⠀⠀⣀⣴⣿⣷⣶⣤⣤⣤⣴⣾⣷⣶⣦⡀ \n⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄ \n⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛",
)


@borg.on(admin_cmd(pattern=r"صاك"))
async def sakk(sakk):
    await sakk.edit(V)


L = (
    "███████▄▄███████████▄\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
    "██████▀░░█░░░░██████▀\n"
    "░░░░░░░░░█░░░░█\n"
    "░░░░░░░░░░█░░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░░▀▀\n"
)


@borg.on(admin_cmd(pattern=r"معارض"))
async def marth(marth):
    await marth.edit(L)



@bot.on(admin_cmd(pattern="مروحيه(?: |$)(.*)"))
async def _(event):
    "جاري تشغيل الهلكوبتر"
    animation_interval = 1.0
    animation_ttl = range(60)
    animation_chars = [
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 👞
                      ╬═╬/▌ 
                      ╬═╬/ \👞""""",
    ]
    event = await edit_or_reply(event, "**بـدء اقـلاع المـروحيـه ...🚁**")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])    


@bot.on(admin_cmd(pattern="ابره(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    Rallsth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    Rallsth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    await edit_or_reply(mention, f"────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█\n▀▀▀▀▄─█─█─█─█─█─█──█▀█\n─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀\n\n**🚹 ╎ تنح واخذ الابره عزيزي 👨🏻‍⚕🤭😂** [{Rallsth}{Rallsth2}](tg://user?id={user.id})")

@bot.on(admin_cmd(pattern="زرفه$"))
async def _(event):
    catevent = await edit_or_reply(event, "**💦 جاي زرف الشخص تف**")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern="جوه الدرج$"))
async def _(event):
    animation_interval = 3
    animation_ttl = range(0, 103)
    animation_chars = [
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "😅`"
            ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 103]
        
        
@bot.on(admin_cmd(pattern="بوسات$"))
async def _(event):
		await event.edit("❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘")
		await asyncio.sleep(1)
		await event.edit("🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘")
		await asyncio.sleep(1)
		await event.edit("💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘")
		await asyncio.sleep(1)
		await event.edit("💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘")
		await asyncio.sleep(1)
		await event.edit("💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘")
		await asyncio.sleep(1)
		await event.edit("💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘")
		await asyncio.sleep(1)
		await event.edit("🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘")
		await asyncio.sleep(1)
		await event.edit("💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘")
		await asyncio.sleep(1)
		await event.edit("💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘")
		await asyncio.sleep(1)
		await event.edit("💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘")
		await asyncio.sleep(1)
		await event.edit("💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘")
		await asyncio.sleep(1)
		await event.edit("💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘")
		await asyncio.sleep(1)
		await event.edit("💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘")
		await asyncio.sleep(1)
		await event.edit("💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘")
		await asyncio.sleep(1)
		await event.edit("️♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘")
		    
@bot.on(admin_cmd(pattern="حمامه$"))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("--------------🕊")
    await event.edit("-------------🕊️")
    await event.edit("------------🕊️")
    await event.edit("-----------🕊️")
    await event.edit("----------🕊️")
    await event.edit("---------🕊️")
    await event.edit("--------🕊️")
    await event.edit("-------🕊️")
    await event.edit("------🕊️")
    await event.edit("-----🕊️")
    await event.edit("----🕊️")
    await event.edit("---🕊️")
    await event.edit("--🕊️")
    await event.edit("-🕊️")
    await event.edit("❤️🕊️")
    await asyncio.sleep(3)
    await event.delete()
    
@bot.on(admin_cmd(pattern="بيبي$"))
async def _(event):
    "متعة الرسوم المتحركة"
    catevent = await edit_or_reply(event, "**جاري جلب بيبي**")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])

@bot.on(admin_cmd(pattern="فواكه$"))
async def _(event):
    event = await edit_or_reply(event, "رياضه")
    deq = deque(list("🍉🍓🍇🍎🍍🍐🍌"))
    for _ in range(20):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
       

@bot.on(admin_cmd(pattern="فراشه$"))
async def _(event):
    event = await edit_or_reply(event, "**فراشه..**")
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)

@bot.on(admin_cmd(pattern="رياضه$"))
async def _(event):
    "أمر الرسوم المتحركة"
    event = await edit_or_reply(event, "رياضه")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(20):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@bot.on(admin_cmd(pattern="قطار$"))
async def _(event):
    "أمر الرسوم المتحركة"
    animation_interval = 0.2
    animation_ttl = range(30)
    event = await edit_or_reply(event, "قطار")
    animation_chars = [
        "**ت**",
        "**تو**",
        "**توتت**",
        "**تووووت**",
        "**توووت**",
        "**تووووت**",
        "**توووووت**",
        "**توووووت**",
        "**توووووووووت**",
        "**توووووووووووت**",
        "**اجه القطار 🚅**",
        "**وخر عن طريق 🚅🚃🚃**",
        "**تووووت 🚅🚃🚃🚃**",
        "**جبنها وجت ويانه 🚅🚃🚃🚃🚃**",
        "**جبناها وجت ويانه 🚅🚃🚃🚃🚃🚃**",
        "**rain🚅🚃🚃🚃🚃🚃🚃**",
        "**بيباي 🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**مو قطار ضيم**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 30])


@bot.on(admin_cmd(pattern="عين$"))
async def _(event):
    animation_interval = 3
    animation_ttl = range(10)
    event = await edit_or_reply(event, "👁👁")
    animation_chars = [
        "👁👁\n  👱🏻‍♂️  =====> ۿـا ، شلونج شخبارج ؟",
        "👁👁\n  👱🏻‍♀️  =====> كولشي تمام",
        "👁👁\n  👱🏻‍♂️  =====> شنو ههاي شفتج 🤤",
        "👁👁\n  👱🏻‍♀️  =====> هاي شبيك",
        "👁👁\n  👱🏻‍♂️  =====> بس حلك 🤤",
        "👁👁\n  👱🏻‍♀️  =====> وخر ",
        "👁👁\n  👱🏻‍♂️  =====> متت 😹",
        "👁👁\n  👱🏻‍♀️  =====> لا تضحك",
        "👁👁\n  👱🏻‍♂️  =====> بس حلك متت 😹🤤",
        "👁👁\n  👱🏻‍♀️  =====> كافي لتضحك😭😒",
        "👁👁\n  👱🏻‍♂️  =====> باع لشفه 🤤",
        "👁👁\n  👱🏻‍♀️  =====> هاي شبيك لتباوع",
        "👁👁\n  👱🏻‍♂️  =====> دولي",
        "👁👁\n  👱🏻‍♂️  =====> رايح بايي",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
    await asyncio.sleep(animation_interval)
    await event.delete()




CMD_HELP.update(
    {
        "تسليه10": """**اسـم الاضـافـه : **`تسليه10`
        
**╮•❐ اوامـر التسليـه والكاريكتـر ❿ ⦂ **

  •  `.سبونج بوب`
  •  `.ثعلب`
  •  `.جلبي`
  •  `.فيل`
  •  `.معصب`
  •  `.مان`
  •  `.صدمه`
  •  `.نادم`
  •  `.ترمب`
  •  `.تشان`
  •  `.همم`
  •  `.معارض`
  •  `.مروحيه`
  •  `.ابره`

**للنســخ : ** __اضغط ع الامـر لنسخـه__"""
    }
)
