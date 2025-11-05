from fastapi import FastAPI, Request
from .models import TelexRequest
from .utils import get_weather

app = FastAPI(
    title="Telex Weather Agent",
    description="AI Agent that provides live weather info integrated with Telex.im",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Telex Weather Agent is running."}

@app.post("/agent/weather")
async def weather_agent(req: TelexRequest):
    """Respond to Telex messages with weather data."""
    location = req.input.get("location", "Lagos")
    data = get_weather(location)
    if "error" in data:
        return {"success": False, "error": data["error"]}
    
    return {
        "success": True,
        "response": f"The weather in {data['location']} is {data['description']} with a temperature of {data['temperature']}°C and humidity of {data['humidity']}%."
    }
