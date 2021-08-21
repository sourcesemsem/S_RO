# KutGif for Z by: @ZedThon

from .. import reply_id as rd
from . import *


@icssbot.on(icss_cmd(outgoing=True, pattern="ث1"))
@icssbot.on(sudo_cmd(pattern="ث1$", allow_sudo=True))
async def tmattheme(icss):
    if icss.fwd_from:
        return
    zel = await rd(icss)
    if tm_attheme:
        icss_caption = f"**{THAMEA}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الاولى 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, tm_attheme, caption=icss_caption, reply_to=zel
        )
