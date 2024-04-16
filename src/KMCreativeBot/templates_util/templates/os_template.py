import os

from KMCreativeBot.templates_util.templates.template import Template


class OsTemplate(Template):
    def __init__(self, template_name: str, template_dir: str, template_describe: str = ''):
        self.template_name: str = template_name
        self.template_dir: str = template_dir
        self.template_describe: str = template_describe

    def get_content(self) -> str:
        template_path = os.path.join(self.template_dir, self.template_name)
        with open(template_path, 'r') as file:
            return file.read()

