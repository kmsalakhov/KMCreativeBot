from abc import ABC, abstractmethod


class Template(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass
