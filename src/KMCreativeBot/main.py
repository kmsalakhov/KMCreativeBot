# Telethon utility #pip install telethon
import os
from typing import List

import resources.messages.messages as messages
from telethon import TelegramClient, events
from telethon.tl.custom import Button

import jinja2

import configparser
import config.path_config as path_config

import datetime  # Library that we will need to get the day and time, #pip install datetime
import requests  # Library used to make requests to external services (the weather forecast one) # pip install requests

# Access credentials


security_config = configparser.ConfigParser()
security_config.read(path_config.SECURITY_CONFIG_PATH)

api_id = int(security_config.get('default', 'api_id'))
api_hash = security_config.get('default', 'api_hash')
BOT_TOKEN = security_config.get('default', 'BOT_TOKEN')

client = TelegramClient(path_config.SESSIONS_PATH, api_id, api_hash).start(bot_token=BOT_TOKEN)


@client.on(events.NewMessage(pattern='(?i)/start'))
async def start(event):
    sender = await event.get_sender()
    sender_id = sender.id
    await client.send_message(sender_id, messages.HELLO_MESSAGE, parse_mode="HTML")

    template_message = messages.CHOOSE_TEMPLATE_MESSAGE
    templates = os.listdir('../../resources/templates/post-templates')
    template_list_with_slash = ['/' + template for template in templates]
    template_message += '\n'.join(template_list_with_slash)

    await client.send_message(sender_id, template_message, parse_mode="HTML")

@client.on(events.NewMessage(pattern='(?i)/youtube-video-template'))
async def fillTemplate(event):
    sender = await event.get_sender()
    sender_id = sender.id
    await client.send_message(sender_id, messages.HELLO_MESSAGE, parse_mode="HTML")

    async with client.conversation(await event.get_chat(), exclusive=True) as conv:
        keyboard = [[Button.inline("{}".format("hello"), "hello")], [Button.inline("{}".format('HELLO'), 'HELLO')]]

        await conv.send_message(messages.CHOOSE_TEMPLATE_MESSAGE, buttons=keyboard, parse_mode='html')
        press = await conv.wait_event(press_event(sender_id))
        choice = str(press.data.decode("utf-8"))
        await conv.send_message(choice, parse_mode='html')

def press_event(user_id):
    return events.CallbackQuery(func=lambda e: e.sender_id == user_id)

if __name__ == '__main__':
    print("bot started")
    client.run_until_disconnected()
