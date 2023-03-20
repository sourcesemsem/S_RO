import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location
from userbot.plugins.sql_helper.globals import gvarstatus

from userbot import bot
from . import *

from ..Config import Config
from ..helpers import get_user_from_event, reply_id
from . import spamwatch

REP_EM = Config.ID_EM or " •❃ "
ID_EDIT = gvarstatus("ID_ET") or "ايدي"

plugin_category = "utils"
LOGS = logging.getLogger(__name__)
async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)    )
    replied_user_profile_photos_count = "لايـوجـد بروفـايـل"
    dc_id = "Can't get dc id"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    photo = await event.client.download_profile_photo(     user_id,     Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",    download_big=True  )
    first_name = (      first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")  )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("لايـوجـد معـرف")
    user_bio = "لاتـوجـد نبـذة" if not user_bio else user_bio
    rotbat = "⌁ من مطورين السورس 𓄂𓆃 ⌁" if user_id == 5502537272 else ("⌁ العضـو 𓅫 ⌁")
    rotbat = "⌁ مـالك الحساب 𓀫 ⌁" if user_id == (await event.client.get_me()).id and user_id != 5502537272  else rotbat
    caption = "✛━━━━━━━━━━━━━✛\n"
    caption += f"<b> {REP_EM}╎الاسـم    ⇠ </b> {full_name}\n"
    caption += f"<b> {REP_EM}╎المعـرف  ⇠ </b> {username}\n"
    caption += f"<b> {REP_EM}╎الايـدي   ⇠ </b> <code>{user_id}</code>\n"
    caption += f"<b> {REP_EM}╎الرتبـــه  ⇠ {rotbat} </b>\n"
    caption += f"<b> {REP_EM}╎الصـور   ⇠ </b> {replied_user_profile_photos_count}\n"
    caption += f"<b> {REP_EM}╎الحساب ⇠ </b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    caption += f"\n<b> {REP_EM}╎البايـو    ⇠ </b> {user_bio} \n"
    caption += f"✛━━━━━━━━━━━━━✛"
    return photo, caption

@bot.on(admin_cmd(pattern="كشف(?:\s|$)([\s\S]*)",))
@bot.on(sudo_cmd(pattern="كشف(?:\s|$)([\s\S]*)", allow_sudo=True))
async def _(event):
    "Gets information of an user such as restrictions ban by spamwatch or cas"
    replied_user = await get_user_from_event(event)
    if not replied_user:
        return
    catevent = await edit_or_reply(event, "᯽︙ جار إحضار معلومات المستخدم اننظر قليلا ⚒️")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_id = replied_user.users[0].id
    first_name = html.escape(replied_user.users[0].first_name)
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their
        # names
        first_name = first_name.replace("\u2060", "")
    # inspired by https://telegram.dog/afsaI181
    common_chats = 1
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = "Couldn't fetch DC ID!"
    if spamwatch:
        ban = spamwatch.get_ban(user_id)
        if ban:
            sw = f"**Spamwatch Banned :** `True` \n       **-**🤷‍♂️**Reason : **`{ban.reason}`"
        else:
            sw = f"**Spamwatch Banned :** `False`"
    else:
        sw = "**Spamwatch Banned :**`Not Connected`"
    try:
        casurl = "https://api.cas.chat/check?user_id={}".format(user_id)
        data = get(casurl).json()
    except Exception as e:
        LOGS.info(e)
        data = None
    if data:
        if data["ok"]:
            cas = "**Antispam(CAS) Banned :** `True`"
        else:
            cas = "**Antispam(CAS) Banned :** `False`"
    else:
        cas = "**Antispam(CAS) Banned :** `Couldn't Fetch`"
    caption = """**معلومات المسـتخدم[{}](tg://user?id={}):
   ⌔︙⚕️ الايدي: **`{}`
   ⌔︙👥**المجموعات المشتركه : **`{}`
   ⌔︙🌏**رقم قاعده البيانات : **`{}`
   ⌔︙🔏**هل هو حساب موثق  : **`{}`
""".format(
        first_name,
        user_id,
        user_id,
        common_chats,
        dc_id,
        replied_user.users[0].restricted,
        sw,
        cas,
    )
    await edit_or_reply(catevent, caption)


@bot.on(admin_cmd(pattern="ايدي(?: |$)(.*)",))
@bot.on(sudo_cmd(pattern="ايدي(?: |$)(.*)", allow_sudo=True))             
async def who(event):
    "Gets info of an user"
    cat = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(cat, "**- لـم استطـع العثــور ع الشخــص**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(            event.chat_id,            photo,            caption=caption,            link_preview=False,            force_document=False,            reply_to=message_id_to_reply,            parse_mode="html",        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")
#كـتابة  @E_7_V
#تعديل وترتيب  @E_7_V
@bot.on(admin_cmd(pattern="رابط الحساب(?:\s|$)([\s\S]*)",))
@bot.on(admin_cmd(pattern="رابط الحساب(?:\s|$)([\s\S]*)", allow_sudo=True))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⌔︙[{tag}](tg://user?id={user.id})")
