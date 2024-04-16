# Telethon utility #pip install telethon
import resources.messages.messages as messages
from telethon import TelegramClient, events
from telethon.tl.custom import Button

import configparser

import datetime  # Library that we will need to get the day and time, #pip install datetime
import requests  # Library used to make requests to external services (the weather forecast one) # pip install requests

# Access credentials
SECURITY_CONFIG_PATH = "../security/tokens/config.ini"

security_config = configparser.ConfigParser()
security_config.read(SECURITY_CONFIG_PATH)

api_id = int(security_config.get('default', 'api_id'))
api_hash = security_config.get('default', 'api_hash')
BOT_TOKEN = security_config.get('default', 'BOT_TOKEN')

client = TelegramClient('../sessions/', api_id, api_hash).start(bot_token=BOT_TOKEN)


@client.on(events.NewMessage(pattern='(?i)/start'))
async def start(event):
    sender = await event.get_sender()
    sender_id = sender.id
    text = messages.HELLO_MESSAGE
    await client.send_message(sender_id, text, parse_mode="HTML")


if __name__ == '__main__':
    print("bot started")
    client.run_until_disconnected()
