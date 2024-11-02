import pandas as pd
import random 

usecols = ["Rainfall"]

weather_data = pd.read_csv("idweather.csv")



def flight_chance():
    random_id = random.randint(1,366)
    risk = random.randint(0,10)
    try:
        wind_speed = weather_data.iloc[random_id]["WindGustSpeed"]
    except:
        wind_speed = 10
    try:
        pressure = weather_data.iloc[random_id]["Pressure9am"]
    except:
        pressure = 1012
    try:
        cloud = weather_data.iloc[random_id]["Cloud9am"]
    except:
        cloud = 5
    try:
        rain = weather_data.iloc[random_id]["Rainfall"]
    except:
        rain = 4

    failure_chance = (risk*0.025)+(wind_speed*0.01)+((pressure-1000)*0.006)+(cloud*0.02)+(rain*0.015)
    return failure_chance, wind_speed,pressure,cloud,rain

fuel = 10
while True:
    if fuel <=0:
        break
    data = flight_chance()
    failure_chance = data[0]  
    wind_speed = data[1]
    pressure = data[2]
    cloud = data[3]
    rain = data[4]
    action = input("Enter command: ")
    if action == "fly":
        if failure_chance<=0.78:
            print("success!", failure_chance)
            fuel-=0.25
        else:
            print("failure", failure_chance)
            fuel-=1.5

    elif action == "stay":
        print("u stayed")
    else:
        print("invalid command")
    fuel-=1

    
        
    
