from jinja2 import Template

import resources.messages.messages as messages
from telethon import TelegramClient, events, Button

import configparser
import config.path_config as path_config
from KMCreativeBot.templates_util.exceptions.no_template_find_exception import NoTemplateFindException
from KMCreativeBot.templates_util.template_managers.template_manager import TemplateManager

from KMCreativeBot.templates_util.template_providers.os_template_provider import OsTemplateProvider
from KMCreativeBot.templates_util.template_providers.template_provider import TemplateProvider

# Access credentials
security_config = configparser.ConfigParser()
security_config.read(path_config.SECURITY_CONFIG_PATH)

api_id = int(security_config.get('default', 'api_id'))
api_hash = security_config.get('default', 'api_hash')
BOT_TOKEN = security_config.get('default', 'BOT_TOKEN')

client = TelegramClient(path_config.SESSIONS_PATH, api_id, api_hash).start(bot_token=BOT_TOKEN)

templates_provider: TemplateProvider = OsTemplateProvider(path_config.TEMPLATES_PATH)
template_manager: TemplateManager = TemplateManager(templates_provider)


# @client.on(events.NewMessage(pattern='(?i)/start'))
# async def start(event):
#     async with client.conversation(await event.get_chat(), exclusive=True) as conv:
#         await conv.send_message(messages.HELLO_MESSAGE)
#         await conv.send_message(template_manager.get_template_choose_message())
#
#         try:
#             template_name = (await conv.get_response()).message
#             template = templates_provider.get_template(template_name)
#
#             await fill_template(conv, template)
#         except NoTemplateFindException:
#             await conv.send_message(messages.NO_TEMPLATE_FIND_MESSAGE.format(template_name))

@client.on(events.NewMessage(pattern='(?i)/start'))
async def start(event):
    template_list = [template.get_name() for template in templates_provider.get_templates()]

    async with client.conversation(await event.get_chat(), exclusive=True) as conv:
        await conv.send_message(messages.HELLO_MESSAGE)

        buttons = [
            [Button.inline(template_name)]
            for template_name in template_list
        ]

        await conv.send_message(
            messages.CHOOSE_TEMPLATE_MESSAGE,
            buttons=buttons
        )

        try:
            template_name = str((await conv.wait_event(events.CallbackQuery())).data.decode('utf-8'))
            # template_name = await conv.get_response()
            template = templates_provider.get_template(template_name)

            await fill_template(conv, template)
        except NoTemplateFindException:
            await conv.send_message(messages.NO_TEMPLATE_FIND_MESSAGE.format(template_name))


async def fill_template(conv, template):
    jin_template = Template(template.get_content())
    variables = template.extract_variables()
    context = {}

    for index, variable in enumerate(variables):
        message = messages.START_DEFINING_MESSAGE if index == 0 else messages.DEFINE_MESSAGE
        await conv.send_message(message.format(variable))

        variable_definition = (await conv.get_response()).message
        context[variable] = variable_definition

    await conv.send_message(messages.FINAL_MESSAGE.format(jin_template.render(context)), parse_mode="markdown")


def press_event(user_id):
    return events.CallbackQuery(func=lambda e: e.sender_id == user_id)


def press_event(user_id):
    return events.CallbackQuery(func=lambda e: e.sender_id == user_id)


if __name__ == '__main__':
    print("bot started")
    client.run_until_disconnected()
