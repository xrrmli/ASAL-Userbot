from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.goblok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(" ANAK GOBLOK!! ")


@register(outgoing=True, pattern='^.Nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("NAH GITU GOBLOK")


@register(outgoing=True, pattern='^.ga(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ENGGA DULU BANG XIXIXI")


@register(outgoing=True, pattern='^.sokab(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("SOKAB CUIH NGENTOT")


CMD_HELP.update({
    "bacotan":
    "`.goblok`\
\nUsage: buat goblokin.\
\n\n`.ga`\
\nUsage: buat nolak.
`.sokab`\
\nUsage: liat ae.\
\n\n`.Nah`\
\nUsage: liat ajaa."
})
