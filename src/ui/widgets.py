from typing import Callable

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, \
    QPushButton

from src import abstract
from src.models import Report


class ReportLabel(QLabel, abstract.Observer):
    _postfix: str

    def __init__(self, source: Callable, *args, postfix: str = "", **kwargs):
        super(ReportLabel, self).__init__(*args, **kwargs)

        self._source = source
        self._postfix = postfix

    def update_state(self, report: Report):
        resource = self._source(report)

        if not self._source(report):
            self.setText("N/A")
            return

        self.setText(f"{resource}{self._postfix}")


class MainWidget(QWidget):
    DEFAULT_WINDOW_SIZE = (320, 180)

    def __init__(self, parent_app, *args,
                 window_size: tuple[int, int] = None,
                 **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)

        if window_size:
            self.setFixedSize(*window_size)
        else:
            self.setFixedSize(*self.DEFAULT_WINDOW_SIZE)

        location_label = ReportLabel(lambda report: report.location)
        temperature_label = ReportLabel(lambda report: report.temperature,
                                        postfix='°C')
        humidity_label = ReportLabel(lambda report: report.humidity,
                                     postfix='%')
        rain_label = ReportLabel(lambda report: report.rain, postfix="mm")
        wind_label = ReportLabel(lambda report: report.wind_speed,
                                 postfix="m/s")

        parent_app.subscribe_labels(location_label, temperature_label,
                                    humidity_label, rain_label, wind_label)

        refresh_button = QPushButton()
        refresh_button.setText("Refresh")

        refresh_button.clicked.connect(parent_app.update)

        self.layout = build_main_layout(self,
                                        location_label,
                                        temperature_label,
                                        humidity_label,
                                        rain_label,
                                        wind_label,
                                        refresh_button)


def build_location_layout(location_label: ReportLabel):
    layout = QHBoxLayout()
    layout.addWidget(location_label)
    return layout


def build_temperature_layout(temperature_label: ReportLabel):
    layout = QHBoxLayout()
    layout.addWidget(temperature_label)
    return layout


def build_meteorological_layout(humidity_label: ReportLabel,
                                rain_label: ReportLabel,
                                wind_label: ReportLabel):
    layout = QHBoxLayout()
    layout.addWidget(humidity_label, alignment=QtCore.Qt.AlignCenter)
    layout.addWidget(rain_label, alignment=QtCore.Qt.AlignCenter)
    layout.addWidget(wind_label, alignment=QtCore.Qt.AlignCenter)
    return layout


def build_main_layout(parent_widget: QWidget, location_label: ReportLabel,
                      temperature_label: ReportLabel,
                      humidity_label: ReportLabel,
                      rain_label: ReportLabel,
                      wind_label: ReportLabel,
                      refresh_button: QPushButton):
    main_layout = QVBoxLayout(parent_widget)

    location = build_location_layout(location_label)
    temperature = build_temperature_layout(temperature_label)
    meteorological = build_meteorological_layout(humidity_label,
                                                 rain_label, wind_label)

    refresh_button_layout = QHBoxLayout()
    refresh_button_layout.addWidget(refresh_button,
                                    alignment=QtCore.Qt.AlignCenter)

    main_layout.addLayout(location)
    main_layout.addLayout(temperature)
    main_layout.addLayout(meteorological)

    main_layout.addLayout(refresh_button_layout)

    return main_layout
