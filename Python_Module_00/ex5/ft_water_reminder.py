def ft_water_reminder():
    input_time = input("Days since last watering: ")
    if (int(input_time) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
