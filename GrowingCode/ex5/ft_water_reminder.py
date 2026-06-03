def ft_water_reminder():
    water = int(input("Days since last watering: "))
    if (water >= 2):
        print("Water the plants!")
    if (water < 2):
        print("Plants are fine")
