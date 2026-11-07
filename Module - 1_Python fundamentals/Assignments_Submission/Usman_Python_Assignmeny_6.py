from tkinter.messagebox import QUESTION
#
# Number Walk: 1 to 20
# RANGE
# QUESTION 1: up with the simplest counted loop.
# 1.  Use a for loop to print every number from 1 to 20, one number per line.
# 2.  Do not write twenty print statements.
# 3.  After the loop, print Loop completed
for i in range(1,20):
    if i > 20:
        break
    print(i, end=' ')
print('loop completed')
# Question:2  Reverse Countdown
# RANGE
# STEP
# Practice a negative step and understand where range() stops.
# 1.  Print numbers from 15 down to 1 using a for loop.
# 2.  Use the third argument of range()
# instead of doing subtraction inside print().
# 3.  After 1, print Go!.
for i in range(15,0,-1):
    print(i, end=' ')
print('loop completed')

# Question:3 Even Number Generator
# RANGE
# STEP
# Generate values directly with range() rather than checking every number.
# 1.  Print all even numbers from 2 to 40.
# 2.  Use a step value so only even numbers are generated.
# 3.  Print the text Even: before each number.
for i in range(2,40):
    print('even', i, end=' ')
# print('loop completed')
    if i%2==0:
      print('loop completed')

# Question:4 Odd Number Generator
# RANGE
# STEP
# Use start, stop and step together.
# 1.  Print all odd numbers from 1 to 39.
# 2.  Do not use an if statement for this question.
# 3.  Make sure 39 is included
for i in range(2,40):
    if i%2!=0:
        print('odd',i, end=' ')
print('loop completed')

# Question:5 Multiples of Five
# RANGE
# Build confidence with a predictable numerical sequence.
# 1.  Print 5, 10, 15 ... up to 100.
# 2.  Use range() so the loop itself generates the multiples.
# 3.  Print each value as Multiple of 5: value

for i in range(1,20):
        print('5 X',i,'=', 5*i)
print('loop completed')
# Question:6 User-Defined Range
# FOR
# RANGE
# Let the user decide the boundaries of the loop.
# 1.  Take a starting number and ending number from the user.
# 2.  Print every integer from start to end, including the ending number.
# 3.  Assume the starting value is smaller than the ending value
x= int(input("Enter starting number: "))
y= int(input("Enter ending number: "))
for i in range(x,y):
    if i > 20:
        break
    print(i, end=' ')
print('loop completed')

# Question:7 Sum from 1 to N
# SUM
# INPUT
# Introduce the accumulator pattern: a variable keeps the running total.
# 1.  Take N from the user.
# 2.  Start total at 0.
# 3.  Use a for loop to calculate 1 + 2 + ... + N.
# 4.  Print the final sum only after the loop ends.
x= int(input("Enter starting number: "))
y= int(input("Enter ending number: "))
i=1
for i in range(x, y):
        if i > y:
            i = i + x
            break

print('loop completed')
print(i, end=' ')
# Question:8 Sum of Even Numbers
# SUM
# %
# Combine arithmetic and a loop to total only selected values.
# 1.  Calculate the sum of all even numbers from 1 to 100.
# 2.  You may generate even values directly with range() OR check each number using %.
# 3.  Print the final sum.
j=1
for i in range(1,10):
    if i%2==0:
        i=i+J
        break
    print(i, end=' ')
print('loop completed')


Question:9