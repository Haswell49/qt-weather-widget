import json

import requests

from src.config import OPEN_WEATHER_API_KEY
from src.models import Report


class ReportDownloader:
    _data: dict

    URI_TEMPLATE = "https://api.openweathermap.org/data/2.5/weather?" \
                   "units=metric&lat={0}&lon={1}&appid={2}"

    def __init__(self):
        self._data = dict()

    def get_report(self, coord: tuple[float, float]) -> Report | None:
        data = self._download(coord)

        if self._data == data:
            return None

        self._data = data

        return Report.from_open_weather(self._data)

    def _download(self, coord: tuple[float, float]) -> dict | None:
        uri = self.URI_TEMPLATE.format(*coord, OPEN_WEATHER_API_KEY)
        response = requests.get(uri)

        if response.status_code != 200:
            return None

        data = json.loads(response.content)

        return data
