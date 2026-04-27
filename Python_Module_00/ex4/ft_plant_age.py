def ft_plant_age():
    input_age = input("Enter plant age in days: ")
    if (int(input_age) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
