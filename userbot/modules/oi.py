from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.ramli(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Nama Gua Ramli`")
    sleep(3)
    await typew.edit("`15cm`")
    sleep(1)
    await typew.edit("`Tinggal Dibogor, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sange`")
    sleep(1)
    await typew.edit("`Mau Ngewe Ga🥺`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.lopyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hei`")
    sleep(3)
    await typew.edit("`I Just Wanna Say`")
    sleep(1)
    await typew.edit("`I LOVE YOU🥺`")
# Create by myself @localheart
