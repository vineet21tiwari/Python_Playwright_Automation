#========================1.Bus Seat Search=========================
#A passenger is looking for one specific seat in a bus.
#1. Loop through seat numbers 1 to 40 using range().
for i in range(1,41):
    if i==23:
        break
print("Requested seat found:",i)

#2. The requested seat number is 23. When seat 23 is reached, print Requested seat found and stop the loop.

#3. After the loop, print Search finished
print("Search Finished")

#===========================2.First Shared Multiple=========================
#Find the earliest number that satisfies two divisibility rules.
#1. Check numbers from 1 to 100.
for i in range(1,101):
#2. Find the first number divisible by both 6 and 8. Print the number and immediately stop.
    if i%6==0 and i%8==0:
#3. Do not continue checking larger numbers after the first match
        break
print("Found the number:",i, "which is divisible by both 6 and 8")

#======================3.Low Battery Alert=======================
#Simulate a battery percentage falling over time.
#1. Generate battery values from 100 down to 0 in steps of 5.
for i in range(100,-1,-5):
# 2. Print each battery percentage until the value reaches 20.
    if i==20:
# 3. At 20, print Low Battery Warning and stop the loop
        print("Low Battery Warning")
        break
print("Battery Percentage:",i)


#========================4.First Passing Score ====================
#A teacher wants to identify the first passing score in a generated range.
#1. Loop through marks from 30 to 60.
for i in range (30,61):
    #2.Passing starts at 40. Print the first mark that satisfies the passing rule.
    if i==40:
#3. Use break immediately after the first passing score is found

        print("Passing mark is:",i)
        break
#===========5.Shopping Budget Crossing============================
# A customer keeps adding items until a spending limit is crossed.
# 1. Generate item prices from 100 to 1000 in steps of 100.
total=0
for i in range(100,1001,100):
    price=int(input("enter price:"))
#2. Keep adding each price to a running total.
    total+=price
# 3.    As    soon as the    total    becomes    greater   than    2000, print    the    current    item    price and total, then    stop
    if total>2000:
        print("current item price and total", total)
        break
#===================6.Square Threshold Finder========================
# Find the first number whose square crosses a threshold.
# 1. Check numbers from 1 to 20.
num=0
for i in range (1,21):
    num=i**2
    print("the square of a number:", i, "is", num)
# 2. Calculate the square of each number.
    if num>=150:
# 3. Print and stop at the first number whose square is greater than 150
        break

#===================7.Maintenance Floor Skip=============================
# An elevator inspection should ignore floors closed for maintenance.
# 1. Loop through floors 1 to 20.
for i in range (1,21):
    if i==4 or i==8 or i==13:
#2. Skip floors 4, 8 and 13 using continue.
        continue
#3. Print Inspection on floor X for every other floor
    print("Inspection on floor",i,"for every other floor")



#=====================8.Odd Ticket Processing=====================
#A service desk should process only odd-numbered tickets.
#1. Loop through ticket numbers 1 to 30.
for i in range (1,31):
    if i%2==0:
        # 2. If a ticket number is even, skip it using continue.
        continue
    # 3. Print Processing ticket X only for odd tickets

    print("Processing ticket", i,"only for odd tickets")


#=======================9.Skip Multiples of Three===================
#Filter out values that match an exclusion rule.
#1. Loop through numbers 1 to 50.
count=0
for i in range (1,51):
    if i%3==0:
#2. Skip every number divisible by 3.
        continue
    count+=i
#3. Count and print how many numbers were actually processed
    print("numbers were actually processed",count)


#=============================10.Qualifying Score Filter==============================
#Only scores at or above the qualifying mark should be processed.
#1. Generate scores from 0 to 100 in steps of 5.
for i in range(0,101,5):
    if i<40:
        # 2. Skip every score below 40 using continue.
        continue
#3. Print Qualified score: X for all remaining values
    print("Qualified score: ",i)


#=====================11.Reserved Employee IDs=============================
#Some generated employee IDs are reserved and must not be assigned.
#1. Loop through IDs from 1001 to 1020.
for i in range (1001,1021):
    if i%5==0:
        continue
    # 2. Treat every ID divisible by 5 as reserved and skip it.
    # 3. Print Assigned ID: X for all non-reserved IDs
    print("Assigned ID", i,"for all non-reserved IDs")

#======================12.Delivery Day Scheduler======================
#A delivery service works for two weeks but does not deliver every seventh day.
#1. Loop through day numbers 1 to 14.
days=[7,14]
for i in range(1,15):
    # 2. Skip days 7 and 14 using a logical or membership-style condition.
    if i in days:
        continue
#3. Print Delivery scheduled - Day X for every other day
    print("Delivery scheduled - Day",i,"for every other day")

#===============================13.Warehouse Box Scan==========================
#Scan boxes in order while ignoring damaged box numbers.
#1. Loop through box numbers 1 to 50.
damaged_boxes=[6,12,18,24,36,42,48]
for i in range(1,51):
    if i in damaged_boxes:
        # 2. Skip boxes divisible by 6 because they are marked damaged.
        continue
    if i==37:
#3. When box 37 is reached, print Priority box found and stop the scan completely
        print("Priority box found:",i)
        break

#=========================14.Game Level Progression=========================
#A game skips bonus-only levels and stops when a target level is reached.
#1. Loop through levels 1 to 30.
for i in range(1,31):
    # 2. Skip every level divisible by 4 using continue.
    if i%4==0:
        continue
#3. When level 23 is reached, print Target level reached and stop the loop
    if i==23:
        print("Target level reached:",i)
        break



#==========================15.Security Checkpoint Route=======================
#A guard moves through checkpoints with some temporarily closed.
#1. Loop through checkpoints 1 to 25.
for i in range(1,26):
#2. Skip checkpoints 5, 10 and 15 because they are closed.
    if i%5==0:
        continue
#3. At checkpoint 22, print Final security checkpoint reached and stop
    if i==22:
        print("Final security checkpoint reached",i)
        break


#=======================16.Odd Number Hunt===========================
#Find a specific kind of number without processing unnecessary values.
#1. Loop through numbers 1 to 100.
for i in range(1,101):
#2. Skip all even numbers using continue.
    if i%2==0:
        continue
#3. Among the remaining values, stop at the first number greater than 30 that is divisible by 7 and print it
    if i>30 and i%7==0:
        print("first number greater than 30 that is divisible by 7:",i)
        break

# ===============================17.Customer Queue Control=============================
# A service counter skips unavailable customers but closes early for an emergency.
# 1. Loop through customer numbers 1 to 40.
customer_served = 0
for i in range(1, 41):

    # 2. Skip every 5th customer and do not count them as served.
    if i % 5 == 0:
        continue
    # 3. When customer 28 is reached, print Emergency closure, stop the loop, and print the number of customers actually served.
    if i == 28:
        print("Emergency closure:", i)
        break
    customer_served+=1
print("Customer found:", customer_served)



#============================18.Temperature Sensor Monitor================================
#Process only warning temperatures and stop at a critical reading.
#1. Generate temperatures from 20 to 60 in steps of 2.
for i in range(20,61,2):
    if i<40:
        continue
#2. Skip every temperature below 40 using continue. For values from 40 to 48, print Warning: X C.
    elif i >= 40 and i<= 48:
        print("Warning:",i,"C")
#3. At the first temperature of 50 or more, print Critical temperature and stop the loop.
    if i>=50:
        print("Critical temperature:",i)
        break


























































