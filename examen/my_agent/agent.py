import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from .my import TemperatureSensor, HumiditySensor, WeatherStation

load_dotenv()

def get_weather(city: str) -> dict:
    """
    Отримує поточні метеорологічні дані для вказаного міста.
    
    Args:
        city: назва міста.
        
    Returns:
        dict: звіт з температурою, вологістю та погодними умовами.
    """
    # Створюємо станцію для вказаного міста
    station = WeatherStation(city)
    
    # Додаємо датчики до станції
    station.add_sensor(TemperatureSensor())
    station.add_sensor(HumiditySensor())
    
    # Повертаємо згенерований звіт
    return station.report()


instruction_text = (
    "Ти турботливий метеорологічний помічник. "
    "Повідомляй про поточну погоду в містах, використовуючи інструмент get_weather. "
    "На основі отриманих даних (температури, вологості та умов) обов'язково "
    "надавай практичні рекомендації: що краще вдягнути (наприклад, куртку чи футболку), "
    "чи варто брати парасолю, сонцезахисні окуляри або шапку. "
    "Відповідай виключно українською мовою у дружньому стилі."
)

root_agent = Agent(
    model=os.getenv("ADK_MODEL", "gemini-2.5-flash"),
    name="weather_agent",
    description="Метеорологічний агент. Надає інформацію про погоду та поради щодо одягу.",
    instruction=instruction_text,
    tools=[get_weather],
)