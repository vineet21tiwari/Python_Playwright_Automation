from tkinter.messagebox import QUESTION

# QUESTION 1: Bus Seat Search
#  Loop through seat numbers 1 to 40 using range().
# 2. The requested seat number is 23. When seat 23 is reached, print Requested seat found and stop the
# loop.
# 3. After the loop, print Search finished

for i in range(1,41):
    if i == 23:
        print('requested seat found',i)
        break

# QUESTION 2:First Shared Multiple
# RANGE
# BREAK
# %
# Find the earliest number that satisfies two divisibility rules.
# 1. Check numbers from 1 to 100.
# 2. Find the first number divisible by both 6 and 8. Print the number and immediately stop.
# 3. Do not continue checking larger numbers after the first match.

for i in range(1,100):
    if i%6 == 0 and i%8 == 0:
        print('requested number found',i)
        break

# QUESTION 3:Low Battery Alert
# RANGE
# BREAK
# STEP
# Simulate a battery percentage falling over time.
# 1. Generate battery values from 100 down to 0 in steps of 5.
# 2. Print each battery percentage until the value reaches 20.
# 3. At 20, print Low Battery Warning and stop the loop.

for i in range(100,0,-5):
    print('battery charge is now at',i,'percent')
    if i == 20:
        print('battery charge is now low at',i,'percent')
        print('battery charge is now low at',i,'percent please recharge it dirty fellow')
        break


# QUESTION 4:FOR
# First Passing Score
# RANGE
# BREAK
# IF
# A teacher wants to identify the first passing score in a generated range.
# 1. Loop through marks from 30 to 60.
# 2. Passing starts at 40. Print the first mark that satisfies the passing rule.
# 3. Use break immediately after the first passing score is found.
for i in range(30,60):
    if  i%40 == 0:
        print('Passing Score is  found',i)
        break


# QUESTION 5:Shopping Budget Crossing
# SUM
# BREAK
# A customer keeps adding items until a spending limit is crossed.
# 1. Generate item prices from 100 to 1000 in steps of 100.
# 2. Keep adding each price to a running total.
# 3. As soon as the total becomes greater than 2000, print the current item price and total, then stop

itemprice =0
for i in range(100,1000,100):
    print('The price of item is',i,'rupees')
    itemprice +=i
    if itemprice >= 2000:
        print('the current item pricr is',i,'and totalitemprice is:',itemprice)
        break

# QUESTION 6:Square Threshold Finder
# RANGE
# BREAK
# **
# Find the first number whose square crosses a threshold.
# 1. Check numbers from 1 to 20.
# 2. Calculate the square of each number.
# 3. Print and stop at the first number whose square is greater than 150

for i in range(1,20):
    print('the square of',i,'number is ',i*i)
    if i*i > 150:
        print('the square of',i,'number is greater than 150 so the loop stops here ',i*i)
        break

# QUESTION 7:Maintenance Floor Skip
# RANGE
# CONTINUE
# An elevator inspection should ignore floors closed for maintenance.
# 1. Loop through floors 1 to 20.
# 2. Skip floors 4, 8 and 13 using continue.
# 3. Print Inspection on floor X for every other floo

for i in range(1,20):

    if i == 4 or i == 8 or i == 13:
        print()
    else: print('This is floor number', i, 'so inspection on', i, 'thfloor ')
    continue

# QUESTION 8:Odd Ticket Processing
# RANGE
# CONTINUE
# %
# A service desk should process only odd-numbered tickets.
# 1. Loop through ticket numbers 1 to 30.
# 2. If a ticket number is even, skip it using continue.
# 3. Print Processing ticket X only for odd tickets.

for i in range(1,30):
    if i %2 == 0 :
        print()
    else: print(i,'This is odd number so odd number ticket is', i, 'skipped ')
    continue

# QUESTION 9:Skip Multiples of Three
# RANGE
# CONTINUE
# COUNT
# Filter out values that match an exclusion rule.
# 1. Loop through numbers 1 to 50.
# 2. Skip every number divisible by 3.
# 3. Count and print how many numbers were actually processed

for i in range(1,50):
    if i %3 == 0 :
        print(i, 'This number is  divisible by 3', 'so  skipped ')
    else: print(i,'This number is not divisible by 3 print', i, 'so not skipped ')
    continue

# QUESTION 10:Qualifying Score Filter
# RANGE
# CONTINUE
# Only scores at or above the qualifying mark should be processed.
# 1. Generate scores from 0 to 100 in steps of 5.
# 2. Skip every score below 40 using continue.
# 3. Print Qualified score: X for all remaining values

for i in range(0,100,5):
    if i >= 40:
        print('qualified scure ',i,'above 40')
        continue

# QUESTION 11:Reserved Employee IDs
# RANGE
# CONTINUE
# %
# Some generated employee IDs are reserved and must not be assigned.
# 1. Loop through IDs from 1001 to 1020.
# 2. Treat every ID divisible by 5 as reserved and skip it.
# 3. Print Assigned ID: X for all non-reserved IDs

for i in range(1001,1020):
    if i %5 == 0 :
        print()
    else: print(i,'qualified Assigned id ',i,'Non Reserved id')
    continue

# QUESTION 12:Delivery Day Scheduler
# RANGE
# CONTINUE
# A delivery service works for two weeks but does not deliver every seventh day.
# 1. Loop through day numbers 1 to 14.
# 2. Skip days 7 and 14 using a logical or membership-style condition.
# 3. Print Delivery scheduled - Day X for every other day

for i in range(1,15):
    if i % 7 == 0 :
        print('skipped')

    elif i%2==0:
        print(i,'Delivery scheduled - Day', i, 'so not skipped ')

# QUESTION 13:Warehouse Box Scan
# BREAK
# CONTINUE
# %
# Scan boxes in order while ignoring damaged box numbers.
# 1. Loop through box numbers 1 to 50.
# 2. Skip boxes divisible by 6 because they are marked damaged.
# 3. When box 37 is reached, print Priority box found and stop the scan completely.

for i in range(1,50):
    if i % 6 == 0 :
        print('Damaged Box')

    elif i%37==0:
        print('Priority Box, box number is ', i, 'so not skipped ')
        break

# QUESTION 14:Game Level Progression
# BREAK
# CONTINUE
# LOGIC
# A game skips bonus-only levels and stops when a target level is reached.
# 1. Loop through levels 1 to 30.
# 2. Skip every level divisible by 4 using continue.
# 3. When level 23 is reached, print Target level reached and stop the loop

for i in range(1,30):
    if i % 4 == 0 :
        print('Bonus only Level so skipped ')
    elif i%23==0:
        print('Target Level Reached  ', i, 'so not skipped ')
        break
    else:
        continue

# QUESTION 15:Security Checkpoint Route
# BREAK
# CONTINUE
# A guard moves through checkpoints with some temporarily closed.
# 1. Loop through checkpoints 1 to 25.
# 2. Skip checkpoints 5, 10 and 15 because they are closed.
# 3. At checkpoint 22, print Final security checkpoint reached and stop.

for i in range(1,25):
    if (i % 5 == 0 and i % 20 != 0) or (i % 10 == 0and i % 20 != 0) or i % 15 == 0  :
        print('we can skip this checkpoint checkpoint number is ',i)
    elif i % 22 == 0:
        print('Final security checkpoint reached this is checkpoint number  ', i, 'so not skipped ')
        break
    else:
        continue