import requests
from .config import OPENWEATHER_API_KEY

def get_weather(location: str):
    """Fetch current weather data for a given location."""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()

        if res.status_code != 200:
            return {"error": data.get("message", "Unable to fetch weather")}

        return {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize(),
        }
    except Exception as e:
        return {"error": str(e)}
