import asyncio
import os
import time
import pyrogram
from cache.admins import admins
from pyrogram import Client, filters
from config import IMG_3, UPDATES_CHANNEL, OWNER_NAME
from driver.filters import command, other_filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(command(["لإعدادات", "لاعدادات", "عدادات", "م"]) & other_filters)
async def nftb(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{IMG_3}",
        caption=f"""🌀 ها هي اوامر الاغاني :
━━━━━━━━━━━━
⇦اوامر تشغيل البوت في المجموعات⇨
⇦ ✪『 تشغيل 』✪➢ ➕ 「اسم الأغنية او / رابط」تشغيل الصوت mp3
⇦ ✪『 فيديو 』✪➢ ➕ 「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
⇦ ✪『 ايقاف او انهاء』✪➢ ☆ لايقاف التشغيل
⇦ ✪『 وقف 』✪➢ ☆ ايقاف التشغيل موقتآ 
⇦ ✪『 تقدم 』✪➢ ☆ تخطي الئ التالي
⇦ ✪『 مواصله 』✪➢ ☆ استئناف التشغيل 
⇦ ✪『 ميوت 』✪➢ ☆ لكتم البوت
⇦ ✪『 الغاء الكتم』✪➢ ☆ لرفع كتم البوت
━━━━━━━━━━━━
⇦اوامر التحكم بلبوت خارج وداخل المجموعات⇨
⇦ ✪『 تحكم 』✪➢ ☆ ↤ تظهر لك قائمة التشغيل
⇦ ✪『 بحث 』✪➢ ➕ «اي شيء تريد البحث عنه بليوتيوب»
⇦ ✪『 الصوت 』✪➢ ➕ «كتابه» الرقم لضبط مستوئ الصوت
⇦ ✪『 تحديث 』✪➢ ☆ لتحديث البوت و قائمة المشرفين
⇦ ✪『 انضم 』✪➢ ☆ لاستدعاء حساب المساعد
⇦ ✪『 مغادرة 』✪➢ ☆ لطرد حساب المساعد 
━━━━━━━━━━━━
⇦اوامر تحكم المطور⇨
⇦ ✪『 مسح 』✪➢ ☆ لمسح جميع الملفات المستخدمه
⇦ ✪『 معلومات  』✪➢ ☆ لرؤيه معلومات النظام 
━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                InlineKeyboardButton("Programmer", url=f"https://t.me/{OWNER_NAME}"),
                ],
            ]
        ),
    )
    
    
@Client.on_message(command(["يدي"]) & other_filters)
def ids(client: Client, message: Message):
    ali = message.reply_to_message
    if ali:
        message.reply_text(
            f"اسمه 🤓: {message.from_user.mention()}\nايديه ☺️: {message.from_user.id}\nيوزره 🌚🙈: @{message.from_user.username}")
    else:
        message.reply(
            f"اسمك 🤓❤️: {message.from_user.mention()}\nايديك ☺️: {message.from_user.id}\nيوزرك 🌚🙈: @{message.from_user.username}"
        )


@Client.on_message(command(["."]) & other_filters)
async def vgdg(client: Client, message: Message):
    await message.reply(
        f""" صلي علي الحبيب ❤️ """
        )


@Client.on_message(command(["جلي"]) & other_filters)
async def nftbs(client: Client, message: Message):
    await message.reply(
        f"""تتشل يبعيد 😹😹
        """)

    
@Client.on_message(command(["نا مين"]) & other_filters)
async def gghpb(client: Client, message: Message):
    await message.reply_text(
        f"""💘 ¦ انت روحي » """, 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "انت روح قلبي🐣💘", url=f"tg://settings")
                ]
            ]
        ),
    )
    
    
@Client.on_message(command(["حبك", "بق", "بكك", "حبق", "بقق", "حبكك"]) & other_filters)
async def nftbs(client: Client, message: Message):
    await message.reply(
        f"""{message.from_user.mention()}بموت فيك يروح قلبي 🥺❤️
        """)
    
    
@Client.on_message(command(["ول"]) & other_filters)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)
    
    
@app.on_message(filters.command(["تبتي"]))
def forward(client, message):
  chat_id = message.chat.id
  user_id = message.from_user.id
  rank = app.get_chat_member(chat_id, user_id)
  rank = rank.status
  if rank == "administrator":
   app.send_message(chat_id,"مسؤول",
   [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ]
                )
  elif rank == "creator":
   app.send_message(chat_id,"المنشئ يعم",
    [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ]
                )
  elif rank == "member":
   app.send_message(chat_id,"عضو زليل",
    [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ]
                )
  elif rank == "restricted":
   app.send_message(chat_id,"عضو متقيد",
    [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ]
                )
  elif rank == "left":
   app.send_message(chat_id,"انتا خرجت يعم",
    [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ]
                )
  elif rank == "kicked":
   app.send_message(chat_id,"الراجل ده واخد بالجزمه ومحظور",
    [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ]
                )

