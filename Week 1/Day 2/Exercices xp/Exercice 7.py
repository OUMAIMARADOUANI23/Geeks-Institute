import random

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10.0, 10.0), 1)
    elif season == "spring":
        return round(random.uniform(10.0, 20.0), 1)
    elif season == "summer":
        return round(random.uniform(20.0, 40.0), 1)
    elif season == "autumn":
        return round(random.uniform(5.0, 25.0), 1)
    else:
        return round(random.uniform(-10.0, 40.0), 1)

def get_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"

def main():
    month = int(input("Enter the month number (1-12): "))
    season = get_season(month)
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    elif 33 <= temp <= 40:
        print("It's really hot! Stay cool.")

main()
