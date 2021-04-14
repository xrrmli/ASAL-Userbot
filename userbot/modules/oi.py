from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.ramli(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**haii nama gua ramlii**")
    sleep(2)
    await typew.edit("**15cm**")
    sleep(2)
    await typew.edit("**tinggal dibogor, salken yaa**")
    sleep(2)
    await typew.edit("**follow ig aku juga @xrrmli**")
    sleep(3)
    await typew.edit("**makasiiii**")
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
