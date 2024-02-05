import json

import requests

from src import abstract
from src.abstract import Observer
from src.config import OPEN_WEATHER_API_KEY
from src.models import Report


class ReportDownloader(abstract.Observable):
    _report: Report | None

    _observers: set[Observer]

    URI_TEMPLATE = "https://api.openweathermap.org/data/2.5/weather?" \
                   "units=metric&lat={0}&lon={1}&appid={2}"

    def __init__(self):
        self._report = None

        self._observers = set()

    def download_report(self, coord: tuple[float, float]):
        data = self._download_data(coord)
        report = Report.from_open_weather(data)

        if self._report == report:
            return None

        self._notify(report)
        self._report = report

    def add_observer(self, observer: Observer):
        self._observers.add(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def _download_data(self, coord: tuple[float, float]) -> dict | None:
        uri = self.URI_TEMPLATE.format(*coord, OPEN_WEATHER_API_KEY)
        response = requests.get(uri)

        if response.status_code != 200:
            return None

        data = json.loads(response.content)

        return data

    def _notify(self, data: Report):
        for observer in self._observers:
            observer.update_state(data)
