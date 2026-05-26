import random
from abc import ABC, abstractmethod
from google.adk.agents.llm_agent import Agent

# ==========================================
# 1. Ієрархія класів для метеостанції (ООП)
# ==========================================

class Sensor(ABC):
    """Абстрактний базовий клас для всіх датчиків."""
    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

    @abstractmethod
    def read(self) -> float:
        """Абстрактний метод для зчитування показників."""
        pass


class TemperatureSensor(Sensor):
    """Датчик температури."""
    def __init__(self):
        super().__init__(name="Температура", unit="°C")

    def read(self) -> float:
        # Повертає випадкову температуру від -15 до 35 °C
        return round(random.uniform(-15.0, 35.0), 1)


class HumiditySensor(Sensor):
    """Датчик вологості."""
    def __init__(self):
        super().__init__(name="Вологість", unit="%")

    def read(self) -> float:
        # Повертає випадкову вологість від 30 до 100 %
        return round(random.uniform(30.0, 100.0), 1)


class WeatherStation:
    """Метеостанція, що збирає дані з різних датчиків."""
    def __init__(self, city: str):
        self.city = city
        self.__sensors = [] # Приватний атрибут (інкапсуляція)

    def add_sensor(self, sensor: Sensor):
        """Додає датчик до метеостанції."""
        self.__sensors.append(sensor)

    def report(self) -> dict:
        """Збирає дані з усіх датчиків та формує звіт."""
        report_data = {
            "city": self.city,
            "temperature_c": None,
            "humidity_percent": None,
            "condition": random.choice(["Сонячно", "Хмарно", "Дощ", "Сніг", "Гроза", "Ясно"])
        }

        # Поліморфізм: викликаємо метод read() у різних типів датчиків
        for sensor in self.__sensors:
            value = sensor.read()
            if isinstance(sensor, TemperatureSensor):
                report_data["temperature_c"] = value
            elif isinstance(sensor, HumiditySensor):
                report_data["humidity_percent"] = value

        return report_data


# ==========================================
# 2. Інструмент для AI-агента (Tool)
# ==========================================

def get_weather(city: str) -> dict:
    """
    Повертає поточну погоду у вказаному місті.
    
    Args:
        city: назва міста
    
    Returns:
        dict: словник з даними про місто, температуру, вологість та умови
    """
    # Створюємо станцію, додаємо датчики і формуємо звіт
    station = WeatherStation(city)
    station.add_sensor(TemperatureSensor())
    station.add_sensor(HumiditySensor())
    
    return station.report()


# ==========================================
# 3. Створення AI-агента
# ==========================================

weather_agent = Agent(
    model='gemini-2.5-flash',
    name='weather_agent',
    description="Метеорологічний помічник, що повідомляє погоду та дає поради щодо одягу.",
    instruction=(
        "Ти турботливий метеорологічний помічник. Твоє завдання — повідомляти про поточну погоду в містах, "
        "використовуючи функцію 'get_weather'. "
        "Отримавши дані про температуру, вологість та погодні умови, ти обов'язково маєш дати користувачу "
        "практичні рекомендації: що краще вдягнути (наприклад, куртку чи футболку), чи варто брати парасолю, "
        "чи потрібні сонцезахисні окуляри тощо. Відповідай українською мовою у дружньому тоні."
    ),
    tools=[get_weather],
)