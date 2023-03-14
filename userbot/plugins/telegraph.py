import pyrogram

import random,os

from pyrogram import Client,filters

from telegraph import Telegraph, upload_file

from pyrogram.types import *

ids = 13740761

hash = "4ce319a92c01fab2b02551af8d7f73a4"

token = "6235699637:AAERB82c_lQN_rWw3LTjdn3vyI5y8MSVh3g" 

app = Client("iraq",api_id=ids,api_hash=hash,bot_token=token)

telegraph = Telegraph()

b = InlineKeyboardMarkup([

    [

    InlineKeyboardButton(text="DEV",url="t.me/E_7_V")

]])

@app.on_message(filters.command("start"))

async def oo(app,msg):

    u = msg.from_user.mention

    await app.send_message(msg.chat.id,f"welcome {u}\nin media to telegraph link bot\njust send media and wait .",reply_markup=b)

@app.on_message(filters.media)

async def upload_to_telegraph(app, message):

    ll = await message.reply("wait . . .")

    kk = ll.id

    if message.media:

        file_name = await message.download()

        telegraph_link = upload_file(file_name)

        link = f"https://graph.org{telegraph_link[0]}"

        await app.delete_messages(message.chat.id,kk)

        await message.reply_text(f"Telegraph link: {link}",disable_web_page_preview=True)

        os.remove(file_name)

    else:

        await message.reply_text("Please upload a media file.")

app.run()
