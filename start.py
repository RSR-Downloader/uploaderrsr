from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("SUPPORT CHANNEL", url="https://t.me/mizolibrary")],
        [InlineKeyboardButton(
            "SUPPORT GROUP", url="https://t.me/rsrmusicofficial")]
    ])
    welcomed = f"Hi! <b>{message.from_user.first_name}</b>Min hmandan tur i hriat duh chuan /help tih hi click rawh."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
