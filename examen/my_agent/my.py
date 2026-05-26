from abc import ABC, abstractmethod
import random
from typing import List, Dict

# Абстрактний клас Sensor
class Sensor(ABC):
    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

    @abstractmethod
    def read(self) -> float:
        pass

class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__(name="Датчик температури", unit="°C")

    def read(self) -> float:
        # Генеруємо випадкову температуру від -20 до +40 градусів
        return round(random.uniform(-20.0, 40.0), 1)

class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__(name="Датчик вологості", unit="%")

    def read(self) -> float:
        # Генеруємо випадкову вологість від 30% до 100%
        return round(random.uniform(30.0, 100.0), 1)

class WeatherStation:
    def __init__(self, city: str):
        self.city = city
        # Інкапсуляція: приватний список датчиків
        self.__sensors: List[Sensor] = []

    def add_sensor(self, sensor: Sensor) -> None:
        self.__sensors.append(sensor)

    def report(self) -> Dict:
        # Базовий словник звіту
        weather_data = {
            "city": self.city,
            "temperature_c": None,
            "humidity_percent": None,
            "condition": random.choice(["Сонячно", "Хмарно", "Дощ", "Сніг", "Гроза", "Ясно"])
        }

        # Поліморфізм: викликаємо метод read() для кожного датчика незалежно від його типу
        for sensor in self.__sensors:
            value = sensor.read()
            if isinstance(sensor, TemperatureSensor):
                weather_data["temperature_c"] = value
            elif isinstance(sensor, HumiditySensor):
                weather_data["humidity_percent"] = value

        return weather_data