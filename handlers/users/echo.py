from loader import dp, bot
from filters import IsPrivate
from aiogram import types,html,F
from data.config import BOT
from keyboards.inline.buttons import add_group_button
import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

DATABASE_FILE = "qorovul.db"
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(30) NULL,
        full_name TEXT,
        telegram_id INTEGER,
        registration_date TEXT
    )
''')
conn.commit()


async def is_user_registered(telegram_id):
    cursor.execute('''
        SELECT telegram_id FROM users WHERE telegram_id=?
    ''', (telegram_id,))
    result = cursor.fetchone()
    return result is not None




silka = html.link(value="silkalarni",link=f"https://t.me/{BOT}?start=true")

text=f'''
Salom👋
<b>Men reklamalarni, yashirin {silka} Guruhlarda o'chirib beraman 👨🏻‍✈️</b>

{html.blockquote(value="<b>Guruhdagi kirdi - chiqdi xabarlarini va hatto tahrirlangan xabarlarni tekshiraman va u reklama boʻlsa oʻchiraman 🤖</b>")}

Men ishlashim uchun Guruhingizga <b>ADMIN</b> qilishingiz kerak😎
'''


@dp.message(IsPrivate(), F.text)
async def echo_bot(message:types.Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    username = message.from_user.username
    is_premium = message.from_user.is_premium
    if not await is_user_registered(telegram_id):
        await message.answer(text=text, reply_markup=add_group_button,disable_web_page_preview=True)

        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''
            INSERT INTO users (username,full_name,telegram_id,registration_date)
            VALUES (?, ?, ?, ?)
        ''', (username,full_name, telegram_id, registration_date))
        conn.commit()
        await bot.send_message(chat_id=-1001810795853,text=f"New 👤: {full_name}\nUsername📩: {f'@{username}' if username else 'None'}\nTelegram 🆔: {html.code(value=telegram_id)}\nReg 📆: {registration_date}\nPremium🤑: {is_premium}",reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Profile", url=f"tg://user?id={telegram_id}")
            ]
        ]
))
    else:
        await message.reply(text=text, reply_markup=add_group_button,disable_web_page_preview=True)


