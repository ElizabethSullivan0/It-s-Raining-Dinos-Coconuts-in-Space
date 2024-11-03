import pandas as pd
import random



# weather_data = pd.read_csv("idweather.csv")
food_data = pd.read_csv("food.csv")
#
#
#
# def flight_chance():
#     random_id = random.randint(1,366)
#     risk = random.randint(0,10)
#     try:
#         wind_speed = weather_data.iloc[random_id]["WindGustSpeed"]
#     except:
#         wind_speed = 10
#     try:
#         pressure = weather_data.iloc[random_id]["Pressure9am"]
#     except:
#         pressure = 1012
#     try:
#         cloud = weather_data.iloc[random_id]["Cloud9am"]
#     except:
#         cloud = 5
#     try:
#         rain = weather_data.iloc[random_id]["Rainfall"]
#     except:
#         rain = 4
#     try:
#         wind_dir = weather_data.iloc[random_id]["WindGustDir"]
#     except:
#         wind_dir = "N/A"
#     #new:
#     try:
#         max_temp = weather_data.iloc[random_id]["MaxTemp"]
#     except:
#         max_temp = 20
#     try:
#         min_temp= weather_data.iloc[random_id]["MinTemp"]
#     except:
#         min_temp = 10

#
#     failure_chance = (risk*0.025)+(wind_speed*0.01)+((pressure-1000)*0.006)+(cloud*0.02)+(rain*0.015)
#     return failure_chance, wind_speed,pressure,cloud,rain,wind_dir,max_temp,min_temp
#
# data =flight_chance()
# failure_chance = data[0]
# wind_speed = data[1]
# wind_dir = data[5]
# pressure = data[2]
# cloud = data[3]
# rain = data[4]
# max_temp= data[5]
# min_temp= data[6]

def gainfood():

    foods = {"Strawberry":0,"Avocado":0,"Spinach":0,"Almond":0,"Pumpkin":0,"Blueberry":0,"Sweet Potato":0,"Honey":0,"Coconut":0,"Lemon":0,"Rice":0,"Quinoa":0,"Olive":0,"Oat":0,"Walnut":0}


    food_id = []
    food_type = []
    for x in range(0,5):
        food_id.append(random.randint(1,14))

    for id in food_id:
        food_type.append(food_data.iloc[id]["FoodItem"])

    for item in food_type:
        amount = random.randint(0,2)
        foods[item] = foods[item] + amount
    return foods
print(gainfood())






