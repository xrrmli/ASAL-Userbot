# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𖣘 𝗛𝗮𝗶 𖣘**")
    await pong.edit("**𖣘𖣘 𝗖𝗮𝗻𝘁𝗶𝗸 𖣘𖣘**")
    await pong.edit("**𖣘𖣘𖣘 𝗡𝗴𝗲𝗻𝘁𝗼𝘁 𖣘𖣘𖣘**")
    await pong.edit("**𖣘𖣘𖣘𖣘 𝗬𝘂𝗸𝗸𝗸 𖣘𖣘𖣘𖣘**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**𖣘𝐏𝐈𝐍𝐆** "
                    f"\n  ➢ `%sms` \n"
                    f"**𖣘𝐁𝐎𝐒𝐒** "
                    f"\n  ➢ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`CROOTTTT💦🥵..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**☠︎︎𝐒𝐀𝐆𝐀𝐏𝐔𝐍𝐆𝐆𝐆🥵💦!**\n"
                    f" **𝐀𝐇𝐇𝐇:** "
                    f"`%sms` \n"
                    f" **𝐂𝐑𝐎𝐎𝐓𝐓𝐓:** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`PUNGG..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⌖ 𝐌𝐘 𝐋𝐎𝐕𝐄𝐄🥰!**\n"
                    f"➷ __𝐏𝐢𝐧𝐠:__ "
                    f"`%sms` \n"
                    f"➷ __𝐔𝐩𝐭𝐢𝐦𝐞:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**🔥**")
    await pong.edit("**🔥🔥**")
    await pong.edit("**🔥🔥🔥**")
    await pong.edit("**PENING!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**𝗣𝗨𝗦𝗜𝗡𝗚**\n"
                    f"**ᴘɪɴɢ:** "
                    f"`%sms` \n"
                    f"**ᴜᴘᴛɪᴍᴇ:** "
                    f"`{uptime}` \n"
                    f"**ᴍᴀsᴛᴇʀ:** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "❃ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "❃ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "❃ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "❃ **Ping:** "
                   f"`{result['ping']}` \n"
                   "❃ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "❃ **BOT:** `Lord Userbot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`TITITT.....🔨`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("➢ **𝐒𝐄𝐏𝐎𝐍𝐆𝐆𝐆🔥🥵**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping` ; `.lping` ; `.xping` ; `.sping`\
    \nUsage: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nUsage: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nUsage: sama kaya perintah ping."
     })
