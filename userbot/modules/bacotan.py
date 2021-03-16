from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.goblok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Goblok Bgt Emg")
    await typew.edit("Anak Goblokk!!")


@register(outgoing=True, pattern='^.ps(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Paansi Babi")
    await typew.edit("Gajelas Goblok")


@register(outgoing=True, pattern='^.ga(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gada-Gada")
    await typew.edit("Pokonya Enggaa")


@register(outgoing=True, pattern='^.skb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Ni Siapa Si Anjing")
    await typew.edit("Sokab Bgt Pepek")


CMD_HELP.update({
    "bacotan":
    "`.goblok`\
\nUsage: buat goblokin.\
\n\n`.ga`\
\nUsage: buat nolak.\
\n\n`.ps`\
\nUsage: paansi.\
\n\n`.skb`\
\nUsage: Liat aja."
})
