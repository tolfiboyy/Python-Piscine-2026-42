def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))

    def count_days_recursive(days):
        if (days <= harvest):
            print(f"Days {days}")
            count_days_recursive(days + 1)
        else:
            print("Harvest time!")
            return
    count_days_recursive(1)
