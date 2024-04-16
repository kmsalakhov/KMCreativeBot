from abc import ABC, abstractmethod
from typing import List


class TemplateProvider(ABC):
    @abstractmethod
    def get_templates(self) -> List[str]:
        pass

    @abstractmethod
    def get_template(self, template_name: str) -> str:
        pass
