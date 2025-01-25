from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_token = os.getenv('BOT_TOKEN')

import nest_asyncio
nest_asyncio.apply()

# Create the client
client = TelegramClient('TGv2', api_id, api_hash)

channel_username = 'ejdailyru'
keywords = set()
channels = set()

bot = await TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/add_keyword (.+)'))
async def add_keyword(event):
    new_keywords = {k.strip().lower() for k in event.pattern_match.group(1).replace(',', ' ').split()}
    keywords.update(new_keywords)
    await event.respond(f'Added keywords: {", ".join(new_keywords)}')


@bot.on(events.NewMessage(pattern='/list_keywords'))
async def list_keywords(event):
    await event.respond(f'Keywords: {", ".join(keywords) or "none"}')

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    if any(k.lower() in event.text.lower() for k in keywords):
        print(f"Keyword found in message: {event.text[:100]}...")
