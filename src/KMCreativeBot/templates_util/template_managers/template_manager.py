from KMCreativeBot.templates_util.template_providers.template_provider import TemplateProvider
import resources.messages.messages as messages


class TemplateManager:
    def __init__(self, template_provider: TemplateProvider):
        self.template_provider: TemplateProvider = template_provider

    def get_template_names_with_slash(self) -> list[str]:
        templates_list = self.template_provider.get_templates()

        return ['/' + template.get_name() for template in templates_list]

    def get_template_choose_message(self) -> str:
        return '{}\n{}'.format(messages.CHOOSE_TEMPLATE_MESSAGE, '\n'.join(self.get_template_names_with_slash()))
