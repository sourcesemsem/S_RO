# Ralls - THON

from telethon.sessions import StringSession as ss
from telethon.sync import TelegramClient as tc

print("𓆩 SOURCE 𝚁𝚎𝚙𝚝𝚑𝚘𝚗 -  STRING SESSION 𓆪")
print("")

API_ID = int(input("⌔∮ ENTER APP ID HERE - "))
API_HASH = input("⌔∮ ENTER API HASH HERE - ")

with tc(ss(), API_ID, API_HASH) as client:
    ics = client.send_message("me", client.session.save())
    ics.reply("⌔∮ هذا هو كود التيرمكس الخاص بك.\n⌔∮ المطور - @ZQ_LO. ")
    print("")
    print("")
    print(
        "⌔∮ Below is the STRING_SESSION. You can also find it in your Telegram Saved Messages."
    )
    print("")
    print("")
    print(client.session.save())
