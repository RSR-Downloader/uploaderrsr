from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Aw le! Youtube Video Mp3/Mp4 engpawh ka download theia, Mahse, Playlists a theih loh thung. Youtube URL Link lo thawn tawp la aw. Chuan Mp3/Mp4 i duh ilo thlang mai ang. Hriatthiam loh i neih chuan Join @rsrmusicofficial"
    await message.reply_text(helptxt)
