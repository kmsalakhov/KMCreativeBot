from abc import ABC, abstractmethod
import re


class Template(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    def extract_variables(self) -> list[str]:
        pattern = r"{{\s*(\w+)\s*}}"

        variables = re.findall(pattern, self.get_content())

        return variables
