import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from utils import is_check_admin
from Script import script
from info import ADMINS


@Client.on_message(filters.command('grp_cmds'))
async def grp_cmds(client, message):
    user_id = message.from_user.id if message.from_user else None
    if not user_id:
        return await message.reply("<b>💔 ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ...</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("<code>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.</code>")
    grp_id = message.chat.id
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('<b>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ</b>')
    #title = message.chat.title
    buttons = [[
                InlineKeyboardButton('✘ ᴄʟᴏsᴇ ✘', callback_data='close_data')
            ]]        
    await message.reply_text(
        text=script.GROUP_C_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.HTML
        )
    

@Client.on_message(filters.command("admin_cmds") & filters.user(ADMINS))
async def admin_cmds(client, message):
    buttons = [
        [KeyboardButton("/refresh"), KeyboardButton("/set_muc")],
        [KeyboardButton("/pm_search_on"), KeyboardButton("/pm_search_off")],
        [KeyboardButton("/set_ads"), KeyboardButton("/del_ads")],
        [KeyboardButton("/setlist"), KeyboardButton("/clearlist")],
        [KeyboardButton("/index")],
        [KeyboardButton("/send"), KeyboardButton("/leave")],
        [KeyboardButton("/ban"), KeyboardButton("/unban")],
        [KeyboardButton("/broadcast"), KeyboardButton("/grp_broadcast")],
        [KeyboardButton("/delreq"), KeyboardButton("/channel")],
        [KeyboardButton("/del_file"), KeyboardButton("/delete")],
        [KeyboardButton("/deletefiles"), KeyboardButton("/deleteall")],
        [KeyboardButton("ᴀʟʟ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ᴏɴʟʏ ʙʏ ᴀᴅᴍɪɴꜱ.")],
        [KeyboardButton("⚡ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴍᴏᴠɪᴇ ᴠᴇʀꜱᴇ")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
   
    sent_message = await message.reply(
        "<b>Admin All Commands [auto delete 2 min] 👇</b>",
        reply_markup=reply_markup,
    ) 
    #  2 minutes (120 seconds)
    await asyncio.sleep(120)
    await sent_message.delete()
    await message.delete()


@Client.on_message(filters.command("commands") & filters.user(ADMINS))
async def set_commands(client, message):
    commands = [
        BotCommand("start", "ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
        BotCommand("most", "ɢᴇᴛ ᴍᴏꜱᴛ ꜱᴇᴀʀᴄʜᴇꜱ ʙᴜᴛᴛᴏɴ ʟɪꜱᴛ"),
        BotCommand("trend", "ɢᴇᴛ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ʙᴜᴛᴛᴏɴ ʟɪꜱᴛ"),
        BotCommand("mostlist", "ꜱʜᴏᴡ ᴍᴏꜱᴛ ꜱᴇᴀʀᴄʜᴇꜱ ʟɪꜱᴛ"),
        BotCommand("trendlist", "ɢᴇᴛ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ʙᴜᴛᴛᴏɴ ʟɪꜱᴛ "),
        BotCommand("stats", "ᴄʜᴇᴄᴋ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ"),
        BotCommand("id", "ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ"),
        BotCommand("font", "ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴏᴏʟ ꜰᴏɴᴛꜱ"),
        BotCommand("details", "ᴄʜᴇᴄᴋ ɢʀᴏᴜᴘ ᴅᴇᴛᴀɪʟꜱ"),
        BotCommand("settings", "ᴄʜᴀɴɢᴇ ʙᴏᴛ ꜱᴇᴛᴛɪɴɢ"),
        BotCommand("grp_cmds", "ᴄʜᴇᴄᴋ ɢʀᴏᴜᴘ ᴄᴏᴍᴍᴀɴᴅꜱ"),
        BotCommand("admin_cmds", "ʙᴏᴛ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ")
    ]
    await client.set_bot_commands(commands)
    await message.reply("Set command successfully")
