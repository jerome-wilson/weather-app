import requests
import json

print("---------------WEATHER APP 1.0---------------")
print("powered by: jerome")
print("enter 0 to exit")
city = input("Enter the city: ")
api = '92ed86888fe44bc183362834241806'
url = f"https://api.weatherapi.com/v1/current.json?key={api}&q={city}"

r = requests.get(url)
# print(r.text)
weather_dict = json.loads(r.text)
while True:
    q = int(input("What do you want to know? \n 1: temperature, 2: condition\n 3: wind speed, 4: humidity\n 5: wind direction, 6: cloud\n 7: Heat Index, 8: Visibility\n 9: UV Index, 10: Pressure\nEnter your choice (1-10): "))
    if q == 0:
        break
    match q:
        case 1:
            print()
            temp1 = weather_dict["current"]["temp_c"]
            temp2 = weather_dict["current"]["temp_f"]
            print("Temperature in celcius: ",temp1)
            print("Temperature in fahrenheit: ",temp2)
            print()
        case 2:
            print()
            condition = weather_dict["current"]["condition"]["text"]
            print("Condition: ",condition)
            print()
        case 3:
            print()
            wind_speed1 = weather_dict["current"]["wind_kph"]
            wind_speed2 = weather_dict["current"]["wind_mph"]
            print("Wind speed in kmph: ",wind_speed1)
            print("Wind speed in mph: ",wind_speed2)
            print()
        case 4:
            print()
            humidity = weather_dict["current"]["humidity"]
            print("Humidity: ",humidity)
            print()
        case 5:
            print()
            wind_dir = weather_dict["current"]["wind_dir"]
            print("Wind direction: ",wind_dir)
            print()
        case 6:
            print()
            cloud = weather_dict["current"]["cloud"]
            print("Cloud: ",cloud)
            print()
        case 7:
            print()
            heat_index1 = weather_dict["current"]["heatindex_c"]
            heat_index2 = weather_dict["current"]["heatindex_f"]
            print("Heat Index in celcius: ",heat_index1)
            print("Heat Index in fahrenheit: ",heat_index2)
            print()
        case 8:
            print()
            visibility1 = weather_dict["current"]["vis_km"]
            visibility2 = weather_dict["current"]["vis_miles"]
            print("Visibility in km: ",visibility1)
            print("Visibility in miles: ",visibility2)
            print()
        case 9:
            print()
            uv = weather_dict["current"]["uv"]
            print("UV Index: ",uv)
            print()
        case 10:
            print()
            pressure = weather_dict["current"]["pressure_mb"]
            print("Pressure (millibars): ",pressure)
            print()
        case _ :
            print()
            print("Invalid input")
            print()
