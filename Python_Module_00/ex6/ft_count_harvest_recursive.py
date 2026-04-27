def ft_count_harvest_recursive():
    input_days_until_harvest = int(input("Days until harvest: "))

    def count_harvest(actual_day):
        if (actual_day > input_days_until_harvest):
            print("Harvest time!")
            return
        else:
            print(f"Day {actual_day}")
            count_harvest(actual_day + 1)

    count_harvest(1)
