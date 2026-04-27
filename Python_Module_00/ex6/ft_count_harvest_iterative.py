def ft_count_harvest_iterative():
    input_days_until_harvest = input("Days until harvest: ")
    for day in range(1, int(input_days_until_harvest) + 1):
        print(f"Day {day}")
    print("Harvest time!")
