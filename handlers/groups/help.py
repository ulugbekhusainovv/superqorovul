from aiogram.filters import Command
from loader import dp,bot
from filters import IsGroup
from aiogram import types, html
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji
import random
from data.config import BOT

@dp.message(Command('help'), IsGroup())
async def start_bot(message:types.Message):
    reaction_list = ["🫡",'🧑🏻‍💻','✊','👍🏻','👌']
    help_ = html.link(value="help",link=f"https://t.me/{BOT}?start=help")
    myBot = html.link(value="botga",link=f"https://t.me/{BOT}?start=true")
    try:
        await bot.set_message_reaction(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reaction=[ReactionTypeEmoji(emoji=random.choice(reaction_list))],
        is_big=False
    )
    except: 
        pass
    user = html.link(value=f"{message.from_user.full_name}", link=f"tg://user?id={message.from_user.id}")
    await message.reply(f'''Salom {user} qanday yordam kerak\n <b>{html.blockquote(value=f"Agar bot ishlashida muammo bo'lsa {myBot} kirib qaytadan {help_} buyug'ini bering")}</b>''',disable_web_page_preview=True)


