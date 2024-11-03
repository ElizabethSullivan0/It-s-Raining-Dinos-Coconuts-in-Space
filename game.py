import pandas as pd
import random
from tabulate import tabulate
from time import sleep
import numpy as np
import matplotlib.pyplot as plt








def print_fast(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.01)
    print() # go to new line

def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.025)
    print() # go to new line
def print_slower(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(1)
    print()


weather_data = pd.read_csv("idweather.csv")
food_data = pd.read_csv("food.csv")


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
    try:
        wind_dir = weather_data.iloc[random_id]["WindGustDir"]
    except:
        wind_dir = "N/A"
    try:
        max_temp = weather_data.iloc[random_id]["MaxTemp"]
    except:
        max_temp = 20
    try:
        min_temp= weather_data.iloc[random_id]["MinTemp"]
    except:
        min_temp = 10

    try:
        temp = random.randint(min_temp,max_temp)
    except:
        temp = 13
    failure_chance = (risk*0.025)+(wind_speed*0.01)+((pressure-1000)*0.006)+(cloud*0.02)+(rain*0.015)
    return failure_chance, wind_speed,pressure,cloud,rain,wind_dir,temp






def info():
    data =flight_chance()
    failure_chance = data[0]
    wind_speed = data[1]
    wind_dir = data[5]
    pressure = data[2]
    cloud = data[3]
    rain = data[4]
    temp = data[6]
    print("------------------\nWeather Stats: \nWind Speed:",wind_speed,"\nWind Direction:",wind_dir,"\npressure:",pressure,"\nCloudiness:",cloud,"\nRaindall:",rain,"\n------------------\nFor more information on weather stats, type: weather_help\n------------------")



def help():
    print("------------------\nList of Commands:\nmain         - direct to main screen\ninfo         - direct to weather info screen\nweather_help - direct to help on weather statistics\nstorage      - direct to storage screen\n------------------")

def weather_help():
    weatherinfo = [["Wind Speed","Knots",0,41,9.71],["Wind Direction","N/A","N/A","N/A","N/A"],["Cloudiness","okta",0,8,3.89],["Rainfall","mm",0,39,8,1.42]]
    print("------------------\n", tabulate(weatherinfo, headers=["Item","Units","MIN","MAX","AVERAGE"], tablefmt="fancy_grid"),"\n------------------")


def intro():
    print_slow(("------------------\nYou're sitting back relaxing in your chair, coconut milk in one hand and some tea in the other, watching the stars go by.\nBut wait...\nThey're going by a bit speedier than you'd expect.... and is that something burning in the air?\n\"NO!!!!!!!\"\n\"OH MY GOD OH MY GOD\"\n\"OHHHHH MY GOD\"\n\"I THINK THE SHIPS ON FIRE\"\nYou calmly come to the realisation the ship is on fire and you are in fact crashing in..."))
    print_slower(("3\n2\n1"))
    print_slow(("You've very much crashed on a strange planet and it is very much not where you'd ideally be.\nMaybe you should think about leaving.\nYou're ship looks pretty messed up though, watch out for the weather?"))
    print("------------------\nOBJECTIVE:\n - Keep exploring planets until you land home\n - Pick up more food along the way (to sell for money for fuel in a future update)\n - Use your console to observe the weather\n - Bad weather conditions will make chance of a succesful flight lower and more fuel will be consumed\n - You're fuel decreases a small amoutn each day regardless of whether you flew\n - DON'T RUN OUT OF FUEL\n------------------\n - Enter help for a list of commands\n------------------")


def gainfood(data):
    temp = (data[6])
    foods = {"Strawberry":0,"Avocado":0,"Spinach":0,"Almond":0,"Pumpkin":0,"Blueberry":0,"Sweet Potato":0,"Honey":0,"Coconut":10,"Lemon":0,"Rice":0,"Quinoa":0,"Olive":0,"Oat":0,"Walnut":0}


    food_id = []
    food_type = []
    for x in range(0,5):
        food_id.append(random.randint(1,14))

    for id in food_id:
        food_type.append(food_data.iloc[id]["FoodItem"])

    for item in food_type:
        min_temp = food_data.iloc[id]["MinTemp"]
        max_temp = food_data.iloc[id]["MaxTemp"]

        if temp<=max_temp and temp>=min_temp:
            amount = random.randint(0,2)
            foods[item] = foods[item] + amount
            print("You found",amount,"pieces of",item)
    return foods





#to be finished, add fly or stay mechanics, take away fuel and add day
def main(fuel,day,planets_visited):
    print("------------------\nMAIN SCREEN\ntype help for commands\n\nTo fly enter: fly\nTo stay enter: stay\n------------------")
    print("Planets visited:",planets_visited)
    mainaction = input("Enter your command: ")
    if mainaction == "fly":
        if data[0]>=0.74:
            rand = random.randint(1,5)
            loss = 0.2 + 0.04*rand
            fuel-=(0.25+loss)
            print("Takeoff failure, conditions too harsh. You've lost",loss,"units of fuel.")

        else:
            print("Takeoff success!!! You have succesfully traveled to the next planet")
            planets_visited+=1
            gainfood(data)
        fuel-=0.4
        day+=1
        print("Some fuel evaporated in the night....\nIt is now day ",day,".\nYou have",fuel,"units of fuel left")
        main(fuel,day,planets_visited)
    elif mainaction == "stay":
        fuel -= 0.4
        day+=1
        print("Some fuel evaporated in the night....\nIt is now day" , day ,".\nYou have", fuel, "units of fuel left")
        main(fuel,day,planets_visited)
    elif mainaction == "main":
        main(fuel,day,planets_visited)
    elif mainaction == "help":
        help()
    elif mainaction == "info":
        info()
    elif mainaction == "weather_help":
        weather_help()
    elif mainaction == "storage":
        storage(foodlist)
    else:
        print("Invalid command")
        main(fuel,day,planets_visited)


def storage(foods):
    # df = pd.DataFrame(foods)
    print("------------------\nYOUR STORAGE:\n",foods,"\n------------------")



def play(fuel,day,planets_visited):
    play_intro = input("Play intro (y/n): ")
    if play_intro == "y":
        intro()
    while True:
        if fuel<=0:
            break
        else:
            action = input("Enter your command: ")
            if action == "main":
                main(fuel,day,planets_visited)
            elif action == "help":
                help()
            elif action == "info":
                info()
            elif action == "weather_help":
                weather_help()
            elif action == "storage":
                storage(foodlist)


fuel = 10
day = 1
planets_visited = 1
data = flight_chance()
failure_chance = data[0]
wind_speed = data[1]
pressure = data[2]
cloud = data[3]
rain = data[4]
foodlist = gainfood(data)


play(fuel,day,planets_visited)
