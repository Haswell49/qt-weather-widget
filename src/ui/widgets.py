from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, \
    QPushButton


class LocationLabel(QLabel):
    def update_location(self, location: str):
        if not location:
            self.setText("N/A")
            return

        self.setText(location)


class TemperatureLabel(QLabel):
    def update_temperature(self, temperature: float):
        if not temperature:
            self.setText("N/A")
            return

        self.setText(f"{temperature}℃")


class WindLabel(QLabel):
    def update_wind(self, wind_speed: int):
        if not wind_speed:
            self.setText("N/A")
            return

        self.setText(f"{wind_speed} m/s")


class HumidityLabel(QLabel):
    def update_humidity(self, humidity: int):
        if not humidity:
            self.setText("N/A")
            return

        self.setText(f"{humidity} %")


class RainLabel(QLabel):
    def update_rain(self, rain: int):
        if not rain:
            self.setText("N/A")
            return

        self.setText(f"{rain} mm")


class MainWidget(QWidget):
    DEFAULT_WINDOW_SIZE = (320, 180)

    _location_label: LocationLabel
    _temperature_label: TemperatureLabel
    _humidity_label: HumidityLabel
    _rain_label: RainLabel
    _wind_label: WindLabel

    _refresh_button: QPushButton

    def __init__(self, parent_app, *args,
                 window_size: tuple[int, int] = None,
                 **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)

        if window_size:
            self.setFixedSize(*window_size)
        else:
            self.setFixedSize(*self.DEFAULT_WINDOW_SIZE)

        self._location_label = LocationLabel()
        self._temperature_label = TemperatureLabel()
        self._humidity_label = HumidityLabel()
        self._rain_label = RainLabel()
        self._wind_label = WindLabel()

        self._refresh_button = QPushButton()
        self._refresh_button.setText("Refresh")

        self._refresh_button.clicked.connect(parent_app.update)

        # self._refresh_button.setEnabled(False)

        self.layout = build_main_layout(self,
                                        self._location_label,
                                        self._temperature_label,
                                        self._humidity_label,
                                        self._rain_label,
                                        self._wind_label,
                                        self._refresh_button)

    def update_ui(self, location: str,
                  temperature: float,
                  humidity: int,
                  rain: int,
                  wind_speed: int):

        self._location_label.setText(location)
        self._temperature_label.update_temperature(temperature)
        self._humidity_label.update_humidity(humidity)
        self._rain_label.update_rain(rain)
        self._wind_label.update_wind(wind_speed)


def build_location_layout(location_label: LocationLabel):
    layout = QHBoxLayout()
    layout.addWidget(location_label)
    return layout


def build_temperature_layout(temperature_label: TemperatureLabel):
    layout = QHBoxLayout()
    layout.addWidget(temperature_label)
    return layout


def build_meteorological_layout(humidity_label: HumidityLabel,
                                rain_label: RainLabel,
                                wind_label: WindLabel):
    layout = QHBoxLayout()
    layout.addWidget(humidity_label, alignment=QtCore.Qt.AlignCenter)
    layout.addWidget(rain_label, alignment=QtCore.Qt.AlignCenter)
    layout.addWidget(wind_label, alignment=QtCore.Qt.AlignCenter)
    return layout


def build_main_layout(parent_widget: QWidget, location_label: LocationLabel,
                      temperature_label: TemperatureLabel,
                      humidity_label: HumidityLabel,
                      rain_label: RainLabel,
                      wind_label: WindLabel,
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
