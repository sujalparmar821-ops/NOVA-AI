"""
COMMANDS/weather.py
-------------------
Weather commands for NOVA.
"""

import requests


# =================================
# DEFAULT LOCATION
# =================================

LATITUDE = 22.5645
LONGITUDE = 72.9289
LOCATION_NAME = "Anand"


# =================================
# COMMON CITY COORDINATES
# =================================

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

    "anand": (22.5645, 72.9289),

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


# =================================
# CITY ALIASES
# =================================

CITY_ALIASES = {

    "amdavad": "ahmedabad",

    "bombay": "mumbai",

    "new delhi": "new delhi",

    "bengaluru": "bengaluru",

    "bangalore": "bangalore",

    "baroda": "vadodara",

    "rajkot city": "rajkot",

    "jamnagar city": "jamnagar",

    "anand city": "anand",
}


# =================================
# GEOCODE CITY
# =================================

def geocode_city(city):

    try:

        city = city.lower().strip()

        city = city.replace(
            " city",
            ""
        ).strip()

        # ---------------------------------
        # ALIAS
        # ---------------------------------

        if city in CITY_ALIASES:

            city = CITY_ALIASES[city]

        # ---------------------------------
        # LOCAL DATABASE FIRST
        # ---------------------------------

        if city in CITIES:

            latitude, longitude = CITIES[city]

            return (
                latitude,
                longitude,
                city.title()
            )

        # ---------------------------------
        # OPEN-METEO GEOCODING
        # ---------------------------------

        geocode_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
        )

        params = {

            "name": city,

            "count": 1,

            "language": "en",

            "format": "json",
        }

        response = requests.get(
            geocode_url,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        results = data.get(
            "results"
        )

        if not results:

            return None

        result = results[0]

        latitude = result.get(
            "latitude"
        )

        longitude = result.get(
            "longitude"
        )

        name = result.get(
            "name"
        )

        country = result.get(
            "country"
        )

        if latitude is None or longitude is None:

            return None

        if country:

            location_name = (
                f"{name}, {country}"
            )

        else:

            location_name = name

        return (
            latitude,
            longitude,
            location_name
        )

    except requests.RequestException as e:

        print(
            f"GEOCODING API ERROR: {e}"
        )

        return None

    except Exception as e:

        print(
            f"GEOCODING ERROR: {e}"
        )

        return None


# =================================
# GET WEATHER
# =================================

def get_weather(city=None):

    try:

        # =================================
        # CHOOSE LOCATION
        # =================================

        if city:

            city = city.lower().strip()

            location = geocode_city(
                city
            )

            if not location:

                return (
                    f"I couldn't find "
                    f"{city}. Please try "
                    f"another city."
                )

            latitude, longitude, location_name = (
                location
            )

        else:

            latitude = LATITUDE

            longitude = LONGITUDE

            location_name = LOCATION_NAME

        # =================================
        # WEATHER API
        # =================================

        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
        )

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

        # =================================
        # CURRENT WEATHER
        # =================================

        current = data.get(
            "current"
        )

        if not current:

            return (
                "I couldn't get the "
                "current weather."
            )

        temperature = current.get(
            "temperature_2m"
        )

        feels_like = current.get(
            "apparent_temperature"
        )

        humidity = current.get(
            "relative_humidity_2m"
        )

        wind = current.get(
            "wind_speed_10m"
        )

        weather_code = current.get(
            "weather_code"
        )

        # =================================
        # WEATHER DESCRIPTION
        # =================================

        condition = weather_description(
            weather_code
        )

        # =================================
        # NOVA RESPONSE
        # =================================

        return (

            f"In {location_name}, "
            f"it's {temperature} "
            f"degrees Celsius with "
            f"{condition}. "

            f"It feels like "
            f"{feels_like} degrees, "

            f"humidity is "
            f"{humidity} percent, "

            f"and wind speed is "
            f"{wind} kilometers "
            f"per hour."
        )

    # =================================
    # API ERROR
    # =================================

    except requests.RequestException as e:

        print(
            f"WEATHER API ERROR: {e}"
        )

        return (
            "I'm unable to get "
            "the weather right now."
        )

    # =================================
    # DATA ERROR
    # =================================

    except (
        KeyError,
        TypeError,
        ValueError
    ) as e:

        print(
            f"WEATHER DATA ERROR: {e}"
        )

        return (
            "I couldn't understand "
            "the weather data."
        )

    # =================================
    # UNKNOWN ERROR
    # =================================

    except Exception as e:

        print(
            f"WEATHER ERROR: {e}"
        )

        return (
            "Something went wrong "
            "while checking the weather."
        )


# =================================
# WEATHER DESCRIPTIONS
# =================================

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