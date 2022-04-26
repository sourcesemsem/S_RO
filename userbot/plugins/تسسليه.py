import asyncio
from collections import deque
from . import ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ralls"


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


@bot.on(admin_cmd(pattern="زرفه$"))
async def _(event):
    catevent = await edit_or_reply(event, "**💦 جاي زرف الشخص تف**")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])

@bot.on(admin_cmd(pattern="زواج$"))
async def _(event):
    catevent = await edit_or_reply(event, "**جاري جلب بيبي**")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])

@bot.on(admin_cmd(pattern="جوه درج$"))
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
            "😅 @RallsThon `"
            ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 103]) 
