from dataclasses import dataclass


@dataclass
class Report:
    _location: str
    _temperature: float
    _humidity: int
    _rain: int
    _wind_speed: int

    def __new__(cls, *args, **kwargs):
        instance = super(Report, cls).__new__(cls)

        cls._generate_properties()

        return instance

    # Generates properties from class fields
    @classmethod
    def _generate_properties(cls):
        cls.location = property(lambda self: self._location)
        cls.temperature = property(lambda self: self._temperature)
        cls.humidity = property(lambda self: self._humidity)
        cls.rain = property(lambda self: self._rain)
        cls.wind_speed = property(lambda self: self._wind_speed)

    def __eq__(self, other):
        if not other:
            return False

        return self.__dict__ == other.__dict__

    @classmethod
    def from_open_weather(cls, data: dict):
        location = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        rain = data["rain"]["1h"] if "rain" in data.keys() else None
        wind_speed = data["wind"]["speed"]

        return cls(location, temperature, humidity, rain, wind_speed)
