from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.k1ck(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Gua Kick Yaaa`")
    sleep(2)
    await typew.edit("`.k1ck`")
    sleep(1)
    await typew.edit("`Tapi Boong Hayuuuu Papale Papale Pap NGENTOT`")
# Create by myself @mentalbrikden


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Da Pa Nich**")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"q
                     "\n**Masi Gua Pantau, Blom Gua Tusbol**")


# Create by myself @localheart

CMD_HELP.update({
    "lord":
    "`.lord`\
    \nUsage: alive bot.\
    \n\n`.k1ck`\
    \nUsage: kick boongan\
    \n\n`.punten` ; `.pantau`\
    \nUsage: coba aja.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya.\
    \n\n`kosong`\
    \nUsage: tunggu update selanjutnya."
})
