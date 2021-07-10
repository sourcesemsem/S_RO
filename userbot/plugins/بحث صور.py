# image search for Icss
import os
import shutil

from ..helpers.google_image_download import googleimagesdownload


@bot.on(admin_cmd(pattern=r"صور(?: |$)(\d*)? ?(.*)"))
@bot.on(sudo_cmd(pattern=r"صور(?: |$)(\d*)? ?(.*)", allow_sudo=True))
async def img_sampler(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await edit_or_reply(
            event, "**╮ الرد ﮼؏ الرسالـٓھہ للبحث او ضعها مع الامر𓅫╰**"
        )
    cat = await edit_or_reply(event, "**╮ ❐ جـاري البحث عن الصـوره 𓅫╰**")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        if lim > 10:
            lim = int(10)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(3)
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    try:
        paths = response.download(arguments)
    except Exception as e:
        return await cat.edit(f"Error: \n`{e}`")
    lst = paths[0][query]
    await event.client.send_file(event.chat_id, lst, reply_to=reply_to_id)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await cat.delete()


CMD_HELP.update(
    {
        "بحث صور": "**Plugin :**`بحث صور`\
    \n\n**  •  Syntax :** `.صور <limit> <name>` او `.صور <limit> (قم برد على الصوره)`\
    \n**  •  Function : **قم بالبحث عن الصور على google وإرسال 3 صور. الافتراضي إذا لم يذكر الحد"
    }
)
