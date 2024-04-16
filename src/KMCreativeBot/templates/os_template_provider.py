import os
from typing import List

from KMCreativeBot.templates.template_provider import TemplateProvider


class OsTemplateProvider(TemplateProvider):
    def __init__(self, template_dir: str):
        self.template_dir = template_dir

    def get_templates(self) -> List[str]:
        return os.listdir(self.template_dir)

    def get_template(self, template_name: str) -> str:
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, 'r') as file:
            return file.read()
