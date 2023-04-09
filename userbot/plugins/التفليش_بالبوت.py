from resources.formation.Config import Config
from userbot import bot
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError


@bot.on(admin_cmd(pattern="حظر_الكل(?:\s|$)([\s\S]*)"))
@bot.on(sudo_cmd(pattern="حظر_الكل(?:\s|$)([\s\S]*)", allow_sudo=True))
async def banall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "حظر"
     is_admin = False
     try:
         partici_ = await bot(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in bot.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await bot.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@bot.on(admin_cmd(pattern="كتم_الكل(?:\s|$)([\s\S]*)"))
@bot.on(sudo_cmd(pattern="كتم_الكل(?:\s|$)([\s\S]*)", allow_sudo=True))
async def muteall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "كتم"
     is_admin = False
     try:
         partici_ = await bot(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in bot.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await jepiq.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass
@bot.on(admin_cmd(pattern="طرد_الكل(?:\s|$)([\s\S]*)"))
@bot.on(sudo_cmd(pattern="طرد_الكل(?:\s|$)([\s\S]*)", allow_sudo=True))
async def kickall(event):
     chat_id = event.chat_id
     if event.is_private:
         return await edit_or_reply(event, "** ᯽︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
     msg = "طرد"
     is_admin = False
     try:
         partici_ = await bot(GetParticipantRequest(
           event.chat_id,
           event.sender_id
         ))
     except UserNotParticipantError:
         is_admin = False
     spam_chats.append(chat_id)
     usrnum = 0
     async for usr in bot.iter_participants(chat_id):
         if not chat_id in spam_chats:
             break
         userb = usr.username
         usrtxt = f"{msg} @{userb}"
         if str(userb) == "None":
             userb = usr.id
             usrtxt = f"{msg} {userb}"
         await bot.send_message(chat_id, usrtxt)
         await asyncio.sleep(1)
         await event.delete()
     try:
         spam_chats.remove(chat_id)
     except:
         pass

@bot.on(admin_cmd(pattern="الغاء التفليش"))
@bot.on(sudo_cmd(pattern="الغاء التفليش", allow_sudo=True))
async def ca_sp(event):
  if not event.chat_id in spam_chats:
    return await edit_or_reply(event, "** ᯽︙ 🤷🏻 لا يوجد طرد او حظر او كتم لأيقافه**")
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await edit_or_reply(event, "** ᯽︙ تم الغاء العملية بنجاح ✓**")
