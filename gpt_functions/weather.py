import random

def get_current_weather(location, unit='celsius'):
    """Mock implementation of a weather retrieval function.
    
    In reality, this would likely use an API to get real weather data.
    """
    # Mock temperature and conditions
    temperature = random.randint(-10, 35) if unit == 'celsius' else random.randint(15, 95)
    conditions = random.choice(['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Windy'])

    return {
        'location': location,
        'unit': unit,
        'temperature': temperature,
        'conditions': conditions,
    }


def get_current_weather_schema():
    return {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"]
                }
            },
            "required": ["location"]
        }
    }

