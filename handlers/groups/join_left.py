import asyncio
from aiogram import types,F,html
from loader import dp
from filters import IsGroup

@dp.message(F.new_chat_members, IsGroup())
async def join_group(message: types.Message):
    joins = message.new_chat_members
    members = ', '.join([html.link(value=f"{m.full_name}", link=f"tg://user?id={m.id}") for m in joins])

    try:
        await message.delete()
        data = await message.answer(f"Xush kelibsiz {members}")
        await asyncio.sleep(5)
        await data.delete()
    except:
        pass

@dp.message(F.left_chat_member, IsGroup())
async def left_group(message: types.Message):
    left_member = message.left_chat_member
    left_person = html.link(value=f"{left_member.full_name}", link=f"tg://user?id={left_member.id}")
    try:
        await message.delete()
        data = await message.answer(f"{left_person} guruhni tark etdi!")
        await asyncio.sleep(3)
        await data.delete()
    except:
        pass