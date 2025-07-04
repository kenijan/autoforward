from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get values from .env
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
source_group = int(os.getenv("SOURCE_GROUP"))
target_group = int(os.getenv("TARGET_GROUP"))

# Create userbot client
client = TelegramClient('user_session', api_id, api_hash)

# Forward message from source_group to target_group
@client.on(events.NewMessage(chats=source_group))
async def forward_message(event):
    try:
        await client.send_message(target_group, event.message)
        print(f"✅ Forwarded message: {event.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Start the bot
print("🚀 UserBot running... waiting for messages...")
client.start()
client.run_until_disconnected()
