# prompts the user for a time

def main():
    current_time = input("What time is it?: ")
    meal_time = convert(current_time)


# outputs either breakfast, lunch or dinner time

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")

    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")

    elif 18.0 <= meal_time <= 19.0:
        print("dinner time")

    else:
        print("")


# converts time, a str in 24-hour format, to the corresponding number of hours as a float
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60



if __name__ == "__main__":
    main()

