# A passenger is looking for one specific seat in a bus.
# 1. Loop through seat numbers 1 to 40 using range().
# 2. The requested seat number is 23. When seat 23 is reached, print Requested seat found and stop the
# loop.
# 3. After the loop, print Search finished
for seat in range(1,41):
    if seat == 23:
        print("Requested seat found")
        break
else:
        print("Requested seat not found")
print("search finsihed")

#7.2
for number in range(1, 101):
    if number % 6 == 0 and number % 8 == 0:
        print(number)
        break
#7.3
    battery_percentage = 100
    while battery_percentage >= 0:
        print(f"Battery: {battery_percentage}%")
        if battery_percentage == 20:
            print("Low Battery Warning")
            break
        battery_percentage -= 5

#7.4
    for mark in range(30, 61):
        if mark >= 40:
            print(f"The first passing score is: {mark}")
            break


#7.5
item_prices = list(range(100, 1001, 100))
total = 0

for price in item_prices:
    total += price
    if total > 2000:
        print(f"Current item price: {price}")
        print(f"Total: {total}")
        break
#7.6
for number in range(1, 21):
    square = number ** 2
    if square > 150:
        print(f"The first number whose square is greater than 150 is: {number}")
        break
#7.7
for floor in range(1, 21):
    if floor in [4, 8, 13]:
        continue
    print(f"Inspection on floor {floor}")
#7.8
    for ticket_number in range(1, 31):
        if ticket_number % 2 == 0:
            continue
        print(f"Processing ticket {ticket_number}")

#7.9
    count = 0
    for number in range(1, 51):
        if number % 3 == 0:
            continue
        count += 1
        print(number)
    print(f"Total numbers processed: {count}")

#7.10
    for score in range(0, 101, 5):
        if score < 40:
            continue
        print(f"Qualified score: {score}")

#7.11
for employee_id in range(1001, 1021):
    if employee_id % 5 == 0:
        continue  # Skip reserved IDs
    print(f"Assigned ID: {employee_id}")

#7.12
    for day in range(1, 15):
        if day == 7 or day == 14:
            continue
        print(f"Delivery scheduled - Day {day}")