import os
import requests
import pandas as pd
import time


# ============================================================
# 1. EXTRACT
# ============================================================

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError(
        "OPENWEATHER_API_KEY was not found. "
        "Please set your API key as an environment variable."
    )


# One representative city for each Nigerian state + FCT
locations = [
    # North Central
    ("Benue", "Makurdi", "North Central"),
    ("Kogi", "Lokoja", "North Central"),
    ("Kwara", "Ilorin", "North Central"),
    ("Nasarawa", "Lafia", "North Central"),
    ("Niger", "Minna", "North Central"),
    ("Plateau", "Jos", "North Central"),
    ("FCT", "Abuja", "North Central"),

    # North East
    ("Adamawa", "Yola", "North East"),
    ("Bauchi", "Bauchi", "North East"),
    ("Borno", "Maiduguri", "North East"),
    ("Gombe", "Gombe", "North East"),
    ("Taraba", "Jalingo", "North East"),
    ("Yobe", "Damaturu", "North East"),

    # North West
    ("Jigawa", "Dutse", "North West"),
    ("Kaduna", "Kaduna", "North West"),
    ("Kano", "Kano", "North West"),
    ("Katsina", "Katsina", "North West"),
    ("Kebbi", "Birnin Kebbi", "North West"),
    ("Sokoto", "Sokoto", "North West"),
    ("Zamfara", "Gusau", "North West"),

    # South East
    ("Abia", "Umuahia", "South East"),
    ("Anambra", "Awka", "South East"),
    ("Ebonyi", "Abakaliki", "South East"),
    ("Enugu", "Enugu", "South East"),
    ("Imo", "Owerri", "South East"),

    # South South
    ("Akwa Ibom", "Uyo", "South South"),
    ("Bayelsa", "Yenagoa", "South South"),
    ("Cross River", "Calabar", "South South"),
    ("Delta", "Asaba", "South South"),
    ("Edo", "Benin City", "South South"),
    ("Rivers", "Port Harcourt", "South South"),

    # South West
    ("Ekiti", "Ado-Ekiti", "South West"),
    ("Lagos", "Ikeja", "South West"),
    ("Ogun", "Abeokuta", "South West"),
    ("Ondo", "Akure", "South West"),
    ("Osun", "Osogbo", "South West"),
    ("Oyo", "Ibadan", "South West")
]


weather_data = []


for state, city, zone in locations:

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": f"{city},NG",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            weather_data.append({
                "City": city,
                "State": state,
                "Country": "Nigeria",
                "Geopolitical_Zone": zone,
                "Temperature_C": data["main"]["temp"],
                "Feels_Like_C": data["main"]["feels_like"],
                "Humidity_%": data["main"]["humidity"],
                "Pressure_hPa": data["main"]["pressure"],
                "Wind_Speed_mps": data["wind"]["speed"],
                "Weather": data["weather"][0]["description"]
            })

            print(f"{state}: data extracted successfully")

        else:
            print(
                f"{state}: extraction failed "
                f"(Status code: {response.status_code})"
            )

    except requests.exceptions.RequestException as error:
        print(f"{state}: request failed - {error}")

    # Prevent sending requests too quickly
    time.sleep(1)


# ============================================================
# 2. TRANSFORM
# ============================================================

weather_df = pd.DataFrame(weather_data)

print("\nData extracted:")
print(weather_df.head())


# Check for missing values
print("\nMissing values:")
print(weather_df.isnull().sum())


# Remove duplicate records if any
weather_df = weather_df.drop_duplicates()


# Sort by geopolitical zone and state
weather_df = weather_df.sort_values(
    ["Geopolitical_Zone", "State"]
).reset_index(drop=True)


print("\nFinal dataset:")
print(weather_df)


# ============================================================
# 3. LOAD
# ============================================================

weather_df.to_csv(
    "weather_data.csv",
    index=False
)

print("\nProcessed dataset saved successfully as weather_data.csv")

print("\nFinal dataset shape:")
print(weather_df.shape)

print("\nETL pipeline completed successfully.")
