from enum import Enum
from typing import Dict


class DescriptionEnum(Enum):
    __descriptions__: Dict[str, str] = {}

    @property
    def description(self) -> str:
        """
        Возвращает описание элемента Enum.
        """
        return self.__descriptions__.get(self.value, None)


class Currency(str, DescriptionEnum):
    """
    Справочник валют
    """

    # TODO добавить все валюты с платформы

    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    __descriptions__ = {
        RUB: "Рубли",
        USD: "Доллары",
        EUR: "Евро",
        GBP: "Фунт стерлингов",
    }

    @classmethod
    def to_dict(cls):
        """
        Метод преобразования enum к словарю
        """
        return {e.name: e.value for e in cls}


class CultureName(str, DescriptionEnum):
    """
    Справочник локализаций
    """

    # TODO добавить все локализации с платформы
    RU = "ru-RU"
    US = "en-US"
    LV = "lv"
    AZ = "az"

    __descriptions__ = {
        RU: "MSK",
        US: "CET",
        LV: "CET",
        AZ: "AZT",
    }
