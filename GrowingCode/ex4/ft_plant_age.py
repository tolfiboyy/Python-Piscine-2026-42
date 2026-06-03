def ft_plant_age():
    harvest = int(input("Enter plant age in days: "))
    if (harvest > 60):
        print("Plant is ready to harvest!")
    if (harvest < 60):
        print("Plant needs more time to grow.")
