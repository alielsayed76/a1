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
            f"اسمه 🤓❤️: {message.from_user.mention()}\nايديه ☺️: {message.from_user.id}\nيوزره 🌚🙈: @{message.from_user.username}"
        )
    else:
        message.reply(
            f"اسمك 🤓❤️: {message.from_user.mention()}\nايديك ☺️: {message.from_user.id}\nيوزرك 🌚🙈: @{message.from_user.username}"
        )


@Client.on_message(command(["."]) & other_filters)
async def vgdg(client: Client, message: Message):
    await message.reply(
        f""" صلي علي الحبيب ❤️ """,
        ),


@Client.on_message(command(["جلي"]) & other_filters)
async def nftb(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{IMG_3}",
        caption=f"""تتشل يبعيد 😹😹
""")
