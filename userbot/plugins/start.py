import random
import logging

from telethon.tl import functions
from userbot import sudo_cmd, admin_cmd
from userbot_utils import sudo_cmd


ownerbaqir_id = 5502537272
@bot.on(admin_cmd(pattern="/start"))
@bot.on(sudo_cmd(pattern=("/start", allow_sudo=True))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerbaqir_id :
        order = await event.reply("اهلا مطوري باقر - @ZQ_LO")
