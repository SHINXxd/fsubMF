import asyncio
from typing import Union
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

async def get_invite_link(bot: Client, chat_id: Union[str, int]):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=chat_id)
        return invite_link
    except FloodWait as e:
        print(f"Sleep of {e.value}s caused by FloodWait ...")
        await asyncio.sleep(e.value)
        return await get_invite_link(bot, chat_id)

async def handle_force_sub(bot: Client, cmd: Message):
    if not Config.FORCE_SUB_CHANNELS:
        return 200

    user_id = cmd.from_user.id

    buttons = []
    for channel_id in Config.FORCE_SUB_CHANNELS:
        try:
            channel_info = await bot.get_chat(channel_id)
            channel_name = channel_info.title
            user = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=user_id,
                    text="Sorry Sir, You are Banned to use me. Contact @Blade_9.",
                    disable_web_page_preview=True
                )
                return 400
        except UserNotParticipant:
            try:
                invite_link = await get_invite_link(bot, chat_id=channel_id)
            except Exception as err:
                print(f"Unable to do Force Subscribe to {channel_id}\n\nError: {err}")
                return 200

            buttons.append(
                [InlineKeyboardButton(f"{channel_name}", url=invite_link.invite_link)]
            )
    
    if not buttons:
        # User is a participant in all channels, return 200 (success)
        return 200

    try:
        await bot.send_message(
            chat_id=user_id,
            text="**Please Join My Updates Channel(s) to use this Bot!**\n\n"
                 "Due to Overload, Only Channel Subscribers can use this Bot!",
            reply_markup=InlineKeyboardMarkup(buttons + [[InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshForceSub")]])
        )
    except Exception:
        await bot.send_message(
            chat_id=user_id,
            text="Something went Wrong. Contact @Blade_9",
            disable_web_page_preview=True
        )
        return 200

    return 400
