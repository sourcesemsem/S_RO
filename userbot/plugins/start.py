import random
import logging

from telethon.tl import functions
from userbot import *
from userbot.utils import sudo_cmd


ownerbaqir_id = 5502537272
@bot.on(admin_cmd(pattern="/start"))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerbaqir_id :
        order = await event.reply("اهلا مطوري باقر - @ZQ_LO")
