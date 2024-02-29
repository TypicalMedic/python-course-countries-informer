from typing import Optional

from geo.clients.shemas import CountryDTO
from geo.clients.weather import WeatherClient
from geo.models import Country


class WeatherService:
    """
    Сервис для работы с данными о погоде.
    """

    def get_weather(self, alpha2code: str, city: str) -> Optional[dict]:
        """
        Получение погоды города.

        :param alpha2code: ISO Alpha2 код страны
        :param city: Город
        :return:
        """

        if data := WeatherClient().get_weather(f"{city},{alpha2code}"):
            return data

        return None
