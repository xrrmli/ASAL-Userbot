@register(outgoing=True, pattern='^.dehan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("Hai Perkenalkan Nama Gua Dehan")
    sleep(3)
    await typew.edit("15cm")
    sleep(1)
    await typew.edit("Tinggal Didepok, Salam Kenal:)")