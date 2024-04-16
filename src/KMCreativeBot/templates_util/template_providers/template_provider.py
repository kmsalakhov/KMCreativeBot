from abc import ABC, abstractmethod
from typing import List

from KMCreativeBot.templates_util.templates.template import Template


class TemplateProvider(ABC):
    @abstractmethod
    def get_templates(self) -> List[Template]:
        pass

    @abstractmethod
    def get_template(self, template_name: str) -> Template:
        pass
