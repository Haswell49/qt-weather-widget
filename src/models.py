from dataclasses import dataclass


@dataclass
class Report:
    _location: str
    _temperature: float
    _humidity: int
    _rain: int
    _wind_speed: int

    def to_tuple(self) -> tuple:
        return (self._location, self._temperature, self._humidity,
                self._rain, self._wind_speed)

    @classmethod
    def from_open_weather(cls, data: dict):
        location = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        rain = data["rain"]["1h"] if "rain" in data.keys() else None
        wind_speed = data["wind"]["speed"]

        return cls(location, temperature, humidity, rain, wind_speed)
