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

















































