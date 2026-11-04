battery_percentage = 100
while battery_percentage >= 0:
    print(f"Battery: {battery_percentage}%")
    if battery_percentage == 20:
        print("Low Battery Warning")
        break
    battery_percentage -= 5 