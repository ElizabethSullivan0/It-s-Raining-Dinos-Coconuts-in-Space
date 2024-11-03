import pandas as pd
import random
from tabulate import tabulate
from time import sleep

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
    try:
        wind_dir = weather_data.iloc[random_id]["WindGustDir"]
    except:
        wind_dir = "N/A"

    failure_chance = (risk*0.025)+(wind_speed*0.01)+((pressure-1000)*0.006)+(cloud*0.02)+(rain*0.015)
    return failure_chance, wind_speed,pressure,cloud,rain,wind_dir



fuel = 10
day = 0
planets_visited = 1
data = flight_chance()
failure_chance = data[0]
wind_speed = data[1]
pressure = data[2]
cloud = data[3]
rain = data[4]


def info():
    data =flight_chance()
    failure_chance = data[0]
    wind_speed = data[1]
    wind_dir = data[5]
    pressure = data[2]
    cloud = data[3]
    rain = data[4]
    print("------------------\nWeather Stats: \nWind Speed:",wind_speed,"\nWind Direction:",wind_dir,"\npressure:",pressure,"\nCloudiness:",cloud,"\nRaindall:",rain,"\n------------------\nFor more information on weather stats, type: weather_help\n------------------")



def help():
    print("------------------\nList of Commands:\nmain         - direct to main screen\ninfo         - direct to weather info screen\nback         - previous screen\nweather_help - direct to help on weather statistics\n------------------")

def weather_help():
    weatherinfo = [["Wind Speed","Knots",0,41,9.71],["Wind Direction","N/A","N/A","N/A","N/A"],["Cloudiness","okta",0,8,3.89],["Rainfall","mm",0,39,8,1.42]]
    print("------------------\n", tabulate(weatherinfo, headers=["Item","Units","MIN","MAX","AVERAGE"], tablefmt="fancy_grid"),"\n------------------")


def intro():
    print_slow(("------------------\nYou're sitting back relaxing in your chair, coconut milk in one hand and some tea in the other, watching the stars go by.\nBut wait...\nThey're going by a bit speedier than you'd expect.... and is that something burning in the air?\n\"NO!!!!!!!\"\n\"OH MY GOD OH MY GOD\"\n\"OHHHHH MY GOD\"\n\"I THINK THE SHIPS ON FIRE\"\nYou calmly come to the realisation the ship is on fire and you are in fact crashing in..."))
    print_slower(("3\n2\n1"))
    print_slow(("You've very much crashed on a strange planet and it is very much not where you'd ideally be.\nMaybe you should think about leaving.\nYou're ship looks pretty messed up though, watch out for the weather?"))
    print("------------------\nOBJECTIVE:\n - Keep exploring planets until you land home\n - Use your console to observe the weather\n - Bad weather conditions will make chance of a succesful flight lower and more fuel will be consumed\n - You're fuel decreases a small amoutn each day regardless of whether you flew\n - DON'T RUN OUT OF FUEL\n------------------")

#to be finished, add fly or stay mecahinics, take away fuel and add day
def main():
    print("------------------\nMAIN SCREEN\ntype help for commands\n\nTo fly enter: fly\nTo stay enter: stay\n------------------")
    mainaction = input("Enter your command: ")
    if mainaction == "fly":
        if data[0]>=0.8:



def play():
    intro()
    while True:
        if fuel<=0:
            break
        else:
            action = input("Enter your command: ")
            if action == "main":
                main()
            elif action == "help":
                help()
            elif action == "info":
                info()
            elif action == "weather_help":
                weather_help()
play()
