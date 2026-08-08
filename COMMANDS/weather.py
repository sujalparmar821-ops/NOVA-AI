"""
COMMANDS/weather.py
-------------------
Weather commands for NOVA.
"""

import requests


# --------------------------------
# Default location
# --------------------------------

LATITUDE = 22.47
LONGITUDE = 70.07
LOCATION_NAME = "Jamnagar"


# --------------------------------
# Common city coordinates
# --------------------------------

CITIES = {
    "ahmedabad": (23.0225, 72.5714),
    "mumbai": (19.0760, 72.8777),
    "delhi": (28.6139, 77.2090),
    "new delhi": (28.6139, 77.2090),
    "surat": (21.1702, 72.8311),
    "vadodara": (22.3072, 73.1812),
    "rajkot": (22.3039, 70.8022),
    "jamnagar": (22.4707, 70.0577),
    "gandhinagar": (23.2156, 72.6369),
    "pune": (18.5204, 73.8567),
    "bangalore": (12.9716, 77.5946),
    "bengaluru": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "jaipur": (26.9124, 75.7873),
    "lucknow": (26.8467, 80.9462),
    "indore": (22.7196, 75.8577),
    "bhopal": (23.2599, 77.4126),
    "goa": (15.2993, 74.1240),
}


def get_weather(city=None):

    try:

        # --------------------------------
        # Choose location
        # --------------------------------

        if city:

            city = city.lower().strip()

            # Remove unnecessary words
            city = city.replace("city", "").strip()

            if city in CITIES:

                latitude, longitude = CITIES[city]

                # Display proper city name
                location_name = city.title()

                if city == "new delhi":
                    location_name = "New Delhi"

                elif city == "bengaluru":
                    location_name = "Bengaluru"

            else:

                return (
                    f"I don't have the coordinates for {city} yet."
                )

        else:

            latitude = LATITUDE
            longitude = LONGITUDE
            location_name = LOCATION_NAME

        # --------------------------------
        # Weather API
        # --------------------------------

        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "apparent_temperature,"
                "relative_humidity_2m,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto",
        }

        response = requests.get(
            weather_url,
            params=weather_params,
            timeout=15,
        )

        response.raise_for_status()

        data = response.json()

        current = data["current"]

        temperature = current["temperature_2m"]
        feels_like = current["apparent_temperature"]
        humidity = current["relative_humidity_2m"]
        wind = current["wind_speed_10m"]
        weather_code = current["weather_code"]

        condition = weather_description(weather_code)

        # --------------------------------
        # NOVA response
        # --------------------------------

        return (
            f"In {location_name}, it's "
            f"{temperature} degrees Celsius "
            f"with {condition}. "
            f"It feels like {feels_like} degrees, "
            f"humidity is {humidity} percent, "
            f"and wind speed is {wind} "
            f"kilometers per hour."
        )

    except requests.RequestException as e:

        print(f"WEATHER API ERROR: {e}")

        return (
            "I'm unable to get the weather right now."
        )

    except (KeyError, TypeError, ValueError) as e:

        print(f"WEATHER DATA ERROR: {e}")

        return (
            "I couldn't understand the weather data."
        )


# --------------------------------
# Weather descriptions
# --------------------------------

def weather_description(code):

    descriptions = {

        0: "clear skies",

        1: "mainly clear skies",

        2: "partly cloudy skies",

        3: "overcast skies",

        45: "foggy conditions",

        48: "foggy conditions",

        51: "light drizzle",

        53: "moderate drizzle",

        55: "heavy drizzle",

        61: "light rain",

        63: "moderate rain",

        65: "heavy rain",

        71: "light snow",

        73: "moderate snow",

        75: "heavy snow",

        80: "light rain showers",

        81: "moderate rain showers",

        82: "heavy rain showers",

        95: "a thunderstorm",

        96: "a thunderstorm with hail",

        99: "a thunderstorm with heavy hail",
    }

    return descriptions.get(
        code,
        "unknown conditions"
    )