from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import BOT

add_group_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ GURUHGA QO'SHISH ➕", url=f"https://t.me/{BOT}?startgroup=true")
        ]
    ]
)


programmer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Dasturchi 🧑🏻‍💻", url=f"https://t.me/ulugbekhusainov")
        ]
    ]
)
