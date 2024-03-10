from aiogram import types, html
from loader import dp,bot
from data.config import BOT
from aiogram.filters import ChatMemberUpdatedFilter,IS_NOT_MEMBER, ADMINISTRATOR,IS_MEMBER
from keyboards.inline.buttons import add_group_button
import sqlite3
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


DATABASE_FILE = "qorovul.db"
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        username VARCHAR(50) NULL,
        title TEXT,
        group_id INTEGER,
        invite_link TEXT NULL,
        registration_date TEXT
    )
''')
conn.commit()

silka = html.link(value="silkalarni",link=f"https://t.me/{BOT}?start=true")
i_am_ready_text = f'''
Salom👋
<b>Men reklamalarni, yashirin {silka} Guruhlarda o'chirib beraman 👨🏻‍✈️</b>

{html.blockquote(value="<b>Guruhdagi kirdi - chiqdi xabarlarini va hatto tahrirlangan xabarlarni tekshiraman va u reklama boʻlsa oʻchiraman 🤖</b>")}

Men guruhda ishlashga <b>tayyorman😎</b>

{html.blockquote(value="<b>🚫Eslatma Men Guruh Adminlari tashlagan reklamalarni o'chirmayman.</b>")}
'''


async def is_group_registered(group_id):
    cursor.execute('''
        SELECT group_id FROM groups WHERE group_id=?
    ''', (group_id,))
    result = cursor.fetchone()
    return result is not None


# #################################################################
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> ADMINISTRATOR))
async def bot_added_as_admin(event: types.ChatMemberUpdated):
    username = event.chat.username
    title = event.chat.title
    group_id = event.chat.id
    chat_type = event.chat.type.title()
    count_users = await bot.get_chat_member_count(chat_id=group_id)
    try:
        invite_link = await bot.export_chat_invite_link(chat_id=group_id)
    except:
        invite_link = None
        
    if not await is_group_registered(group_id):
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO groups (username,title,group_id,invite_link,registration_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, title, group_id, invite_link, registration_date))
        conn.commit()
        msg = f"""
{html.code(value=chat_type)}
<b>Name:</b> {title}
<b>Username:</b> {f"@{username}" if username else 'None'}
<b>{chat_type}🆔:</b> {html.code(value=group_id)}
<b>Reg 📆:</b> {registration_date}
<b>Members 👤:</b> {count_users}
"""
        await bot.send_message(chat_id=-1001810795853,text=msg,
        reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{chat_type}", url=invite_link if invite_link else 'https://t.me/ulugbekhusain'),
            ],
            [
                InlineKeyboardButton(text="Refresh",callback_data=f"refresh:{group_id}"),
                InlineKeyboardButton(text="Leave Chat", callback_data=f'leavechat:{group_id}'),
            ]
        ]

))
    await event.answer(
        text=i_am_ready_text,reply_markup=add_group_button,disable_web_page_preview=True
    )


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_MEMBER >> ADMINISTRATOR)
)
async def bot_added_as_admin(event: types.ChatMemberUpdated):
    username = event.chat.username
    title = event.chat.title
    group_id = event.chat.id
    chat_type = event.chat.type.title()
    count_users = await bot.get_chat_member_count(chat_id=group_id)
    try:
        invite_link = await bot.export_chat_invite_link(chat_id=group_id)
    except:
        invite_link = None
    if not await is_group_registered(group_id):
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO groups (username,title,group_id,invite_link,registration_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, title, group_id, invite_link, registration_date))
        conn.commit()
        msg = f"""
{html.code(value=chat_type)}
<b>Name:</b> {title}
<b>Username:</b> {f"@{username}" if username else 'None'}
<b>{chat_type}🆔:</b> {html.code(value=group_id)}
<b>Reg 📆:</b> {registration_date}
<b>Members 👤:</b> {count_users}
"""
        await bot.send_message(chat_id=-1001810795853,text=msg,
        reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{chat_type}", url=invite_link if invite_link else 'https://t.me/ulugbekhusain'),
            ],
            [
                InlineKeyboardButton(text="Refresh",callback_data=f"refresh:{group_id}"),
                InlineKeyboardButton(text="Leave Chat", callback_data=f'leavechat:{group_id}'),
            ]
        ]

))
    await event.answer(
        text=i_am_ready_text,reply_markup=add_group_button,disable_web_page_preview=True
    )



        
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> IS_MEMBER)
)
async def bot_added_as_admin(event: types.ChatMemberUpdated):
    await event.answer(
        text=f'''
Salom👋
<b>Men reklamalarni, yashirin {silka} Guruhlarda o'chirib beraman 👨🏻‍✈️</b>

{html.blockquote(value="<b>Guruhdagi kirdi - chiqdi xabarlarini va hatto tahrirlangan xabarlarni tekshiraman va u reklama boʻlsa oʻchiraman 🤖</b>")}

Men ishlashim uchun Guruhingizga <b>ADMIN</b> qilishingiz kerak😎
''',
reply_markup=add_group_button ,disable_web_page_preview=True
    )






@dp.callback_query(lambda query: query.data.startswith("refresh:"))
async def refresh_group_info(callback_query: types.CallbackQuery):
    try:
        _, group_id = callback_query.data.split(":")
        group_id = int(group_id)
        get_chat = await bot.get_chat(group_id)
        title = get_chat.title
        username = get_chat.username
        chat_type = get_chat.type.title()
        count_users = await bot.get_chat_member_count(chat_id=group_id)
        try:
            invite_link = await bot.export_chat_invite_link(chat_id=group_id)
        except:
            invite_link = None
        edit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
        refreshed_group_text = f"""
{html.code(value=chat_type)}
<b>Name:</b> {title}
<b>Username:</b> {f"@{username}" if username else 'None'}
<b>{chat_type}🆔:</b> {html.code(value=group_id)}
<b>Editing ✍️:</b> {edit_date}
<b>Members 👤:</b> {count_users}
"""
        await bot.edit_message_text(chat_id=callback_query.message.chat.id, 
                                    message_id=callback_query.message.message_id,
                                    text=refreshed_group_text,
                                    reply_markup=InlineKeyboardMarkup(
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text=f"{chat_type}", url=invite_link if invite_link else 'https://t.me/ulugbekhusain'),
                                        ],
                                        [
                                            InlineKeyboardButton(text="Refresh",callback_data=f"refresh:{group_id}"),
                                            InlineKeyboardButton(text="Leave Chat", callback_data=f'leavechat:{group_id}'),
                                        ]
                                    ]
                                    ))
    except Exception as error:
        print(error)
@dp.callback_query(lambda query: query.data.startswith("leavechat:"))
async def leavechat(callback_query: types.CallbackQuery):
    try:
        _, group_id = callback_query.data.split(":")
        group_id = int(group_id)
        success = await bot.leave_chat(chat_id=group_id)
        if success:
            await callback_query.answer("Muvafaqiyatli✅",show_alert=True)
        else:
            await callback_query.answer("Xatolik yuz berdi. Qayta urinib ko'ring⛔︎",show_alert=True)
    except:
        pass
