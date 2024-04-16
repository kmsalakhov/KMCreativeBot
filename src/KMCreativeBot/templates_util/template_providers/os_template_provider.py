import os
from typing import List

from KMCreativeBot.templates_util.exceptions.no_template_find_exception import NoTemplateFindException
from KMCreativeBot.templates_util.template_providers.template_provider import TemplateProvider
from KMCreativeBot.templates_util.templates.os_template import OsTemplate


class OsTemplateProvider(TemplateProvider):
    def __init__(self, template_dir: str):
        self.template_dir = template_dir
        self.template_dirs = os.listdir(self.template_dir)

    def get_templates(self) -> List[OsTemplate]:
        return [OsTemplate(template_name, self.template_dir) for template_name in self.template_dirs]

    def get_template(self, template_name: str) -> OsTemplate:
        if template_name in self.template_dirs:
            return OsTemplate(template_name, self.template_dir)
        else:
            raise NoTemplateFindException("Cannot find exception with name {}".format(template_name))
