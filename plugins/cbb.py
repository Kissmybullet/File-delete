#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>𝙕𝙚𝙣𝙞𝙩𝙨𝙪 ѦƑ 🥂✨</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/guardians_Bot_Updates'>Albert Ɓºť</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Entertainment_AG'>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('💫 Movies 💫', url='https://t.me/Entertainment_AG')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

# ɪ ᴀᴍ ɴᴏᴛ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʙᴇɪɴɢ ʏᴏᴜʀ sᴇᴄᴏɴᴅ ғᴀᴛʜᴇʀ ... sᴏ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴍʏ ᴄʀᴇᴅɪᴛ...

#⋗  ᴛᴇʟᴇɢʀᴀᴍ - @Codeflix_bots

#ᴛʜɪs ʟɪɴᴇ ɪs ғᴏʀ ᴄᴏᴘʏ-ᴘᴀsᴛᴇʀs...
#...ᴡʜɪʟᴇ ʏᴏᴜ ᴀʀᴇ ʀᴇᴍᴏᴠɪɴɢ ᴍʏ ᴄʀᴇᴅɪᴛ ᴀɴᴅ ᴄᴀʟʟɪɴɢ ʏᴏᴜʀsᴇʟғ ᴀ ᴅᴇᴠᴇʟᴏᴘᴇʀʀ...
 # _____ ᴊᴜsᴛ ɪᴍᴀɢɪɴᴇ, Aᴛ ᴛʜᴀᴛ ᴛɪᴍᴇ ɪ ᴀᴍ ғᴜᴄᴋɪɴɢ ʏᴏᴜʀ ᴍᴏᴍ ᴀɴᴅ sɪs ᴀᴛ sᴀᴍᴇ ᴛɪᴍᴇ, ʜᴀʀᴅᴇʀ & ᴛᴏᴏ ʜᴀʀᴅᴇʀ...

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ ᴄᴏᴅᴇғʟɪx ʙᴏᴛs ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @codeflix_bots Community @Otakflix_Network </b>
