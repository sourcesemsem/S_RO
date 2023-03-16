#RallsThon ®

import asyncio

import glob

import io

import os

import re

import pathlib

from time import time

import requests

try:

    from pyquery import PyQuery as pq

except ModuleNotFoundError:

    os.system("pip3 install pyquery")

    from pyquery import PyQuery as pq

import asyncio

import glob

import io

import os

import re

import pathlib

from time import time

import requests

try:

    from pyquery import PyQuery as pq

except ModuleNotFoundError:

    os.system("pip3 install pyquery")

    from pyquery import PyQuery as pq
    from yt_dlp import yt_dlp, *
    

@bot.on(baqir_cmd(pattern="فيس(?:\s|$)([\s\S]*)",command=("فيسبوك", plugin_category),
@bot.on(sudo_cmd(pattern="فيس(?:\s|$)([\s\S]*)",command=("فيسبوك", plugin_category, All_sudo= True),

info={

        "header": "تحميـل مقـاطـع الفيـديــو مـن فيـس بــوك عـبر الرابـط",

        "مثــال": [

            "{tr}فيس بالــرد ع رابــط",

            "{tr}فيس + رابــط",

        ],

    },

)

async def download_video(event):

    """To download video from YouTube and many other sites."""

    msg = event.pattern_match.group(1)

    rmsg = await event.get_reply_message()

    if not msg and rmsg:

        msg = rmsg.text

    urls = extractor.find_urls(msg)

    if not urls:

        return await edit_or_reply(event, "**- قـم بادخــال رابـط مع الامـر او بالــرد ع رابـط ليتـم التحميـل**")

    bot = await edit_or_reply(event, "**⎉╎جـارِ التحميل مـن فيـس بـوك انتظر قليلا ▬▭ ...**")

    reply_to_id = await reply_id(event)

    for url in urls:

        ytdl_data = await ytdl_down(zedevent, video_opts, url)

        if ytdl_down is None:

            return

        try:

            f = pathlib.Path("cat_ytv.mp4")

            print(f)

            catthumb = pathlib.Path("cat_ytv.jpg")

            if not os.path.exists(catthumb):

                catthumb = pathlib.Path("cat_ytv.webp")

            if not os.path.exists(catthumb):

                catthumb = None

            await bot.edit(

                f"**╮ ❐ جـارِ التحضيـر للـرفع انتظـر ...𓅫╰**:\

                \n**{ytdl_data['title']}**"

            )

            ul = io.open(f, "rb")

            c_time = time()

            attributes, mime_type = await fix_attributes(

                f, ytdl_data, supports_streaming=True

            )

            uploaded = await event.client.fast_upload_file(

                file=ul,

                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(

                    progress(

                        d, t, zedevent, c_time, "Upload :", file_name=ytdl_data["title"]

                    )

                ),

            )

            ul.close()

            media = types.InputMediaUploadedDocument(

                file=uploaded,

                mime_type=mime_type,

                attributes=attributes,

            )

            await event.client.send_file(

                event.chat_id,

                file=med
