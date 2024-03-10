from aiogram.filters import Command
from loader import dp,bot
from aiogram import types
from keyboards.inline.buttons import programmer
from filters import IsPrivate
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji
import random

help_text = """Sizga qanday yordam kerak"""


@dp.message(Command('help'), IsPrivate())
async def help_bot(message:types.Message):
    reaction_list = ["🫡",'🧑🏻‍💻','✊','👍🏻','👌']
    try:
        await bot.set_message_reaction(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reaction=[ReactionTypeEmoji(emoji=random.choice(reaction_list))],
        is_big=False
    )
    except: 
        pass
    await message.reply(help_text, reply_markup=programmer)
