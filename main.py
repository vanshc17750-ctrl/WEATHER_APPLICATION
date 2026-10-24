import requests

a = input("ENTER NAME OF CITY :").upper()
def get_cordinate(city):
    try:
        geocoding = "https://geocoding-api.open-meteo.com/v1/search"
        response = requests.get(
            geocoding,
            params={"name": city }, 
            timeout= 7)
        response.raise_for_status()
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print("API ne valid JSON data nahi bheja.")
            exit()
    except requests.RequestException:
        print("Website ch dikkat aa")
        exit()
    if not data.get("results"):
        print("City not found")
        return None

    item = data["results"][0]
    return item["latitude"], item["longitude"]

def get_weather(city, lat, lon):            
    try:
        weather ="https://api.open-meteo.com/v1/forecast"
        reponse1 = requests.get(weather, 
                                params={"latitude" : lat,
                                "longitude" : lon , 
                                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"}, 
                                timeout=7)
        reponse1.raise_for_status()
        try:
            data1 = reponse1.json()
        except requests.exceptions.JSONDecodeError:
                print("API ne valid JSON data nahi bheja.")
                exit()
    except requests.RequestException:
        print("Website ch dikkat aa")
        exit()
    print(f"CITY : {city}")
    if data1.get("current", {}).get("temperature_2m") is not None:
        print(f"TEMPRATURE : {data1['current']['temperature_2m']}{data1['current_units']['temperature_2m']}")
    else:
        print("NO DATA FOUND")
    if data1.get("current", {}).get("relative_humidity_2m") is not None:
        print(f"HUMIDITY : {data1['current']['relative_humidity_2m']}{data1['current_units']['relative_humidity_2m']}")
    else:
        print("NO DATA FOUND")
    if data1.get("current", {}).get("wind_speed_10m") is not None:
        print(f"WIND-SPEED : {data1['current']['wind_speed_10m']}{data1['current_units']['wind_speed_10m']}")
    else:
        print("NO DATA FOUND")

coordinates = get_cordinate(a)

if coordinates is not None:
    lat, lon = coordinates
    get_weather(a, lat, lon)
