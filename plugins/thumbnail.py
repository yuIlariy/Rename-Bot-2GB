from pyrogram import Client, filters 
from helper.database import jishubotz
import asyncio

@Client.on_message(filters.private & filters.command('viewthumb'))
async def viewthumb(client, message):    
    thumb = await jishubotz.get_thumbnail(message.from_user.id)
    if thumb:
        sent_msg = await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        sent_msg = await message.reply_text("**You Don't Have Any Thumbnail ❌**", quote=True)
    await asyncio.sleep(30)
    await sent_msg.delete()
    await message.delete()

@Client.on_message(filters.private & filters.command('delthumb'))
async def removethumb(client, message):
    await jishubotz.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Thumbnail Deleted Successfully 🗑️**", quote=True)

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("Please Wait ...", quote=True)
    await jishubotz.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("**Thumbnail Saved Successfully ✅️**")
    await asyncio.sleep(30)
    await message.delete()
    await mkn.delete()
