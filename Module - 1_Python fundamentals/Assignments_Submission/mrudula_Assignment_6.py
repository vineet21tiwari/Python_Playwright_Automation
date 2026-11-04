#================1.Number Walk: 1 to 20===================
#1.  Use a for loop to print every number from 1 to 20, one number per line.
for i in range(1,21):
    print(i)
    #print(i, end=" ")
print("Loop completed")

#2.  Do not write twenty print statements.
#3.  After the loop, print Loop completed.

#================2.Reverse Countdown===============================
#1.  Print numbers from 15 down to 1 using a for loop.
for i in range(15,0,-1):
    print(i)
#2.  Use the third argument of range() instead of doing subtraction inside print().
#3.  After 1, print Go!


#===================3.Even Number Generator========================
#Generate values directly with range() rather than checking every number.
#1.  Print all even numbers from 2 to 40.
i=0
for i in range(2,41,2):
    if i%2==0:
        print("Even Number:", i)
#2.  Use a step value so only even numbers are generated.
#3.  Print the text Even: before each number

#==================== 4. Odd Number Generator ====================

# Print all odd numbers from 1 to 39.
for i in range(1, 40, 2):
    print("Odd Number:", i)


#==================== 5. Multiples of Five ====================

# Print multiples of 5 from 5 to 100.
for i in range(5, 101, 5):
    print("Multiple of 5:", i)


#==================== 6. User-Defined Range ====================

# Take starting and ending numbers from the user.
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

# Print every integer from start to end, including the ending number.
for i in range(start, end + 1):
    print(i)

#==================== 7. Sum from 1 to N ====================

# Take N from the user.
n = int(input("Enter a number: "))

# Start total at 0.
total = 0

# Calculate the sum from 1 to N.
for i in range(1, n + 1):
    total += i

# Print the final sum.
print("Sum:", total)


#==================== 8. Sum of Even Numbers ====================

# Start total at 0.
total = 0

# Calculate the sum of even numbers from 1 to 100.
for i in range(2, 101, 2):
    total += i

# Print the final sum.
print("Sum of Even Numbers:", total)


#==================== 9. Multiples-of-Three Total ====================

# Start total and count at 0.
total = 0
count = 0
i=0
# Loop from 1 to 60.
for i in range(1, 61):
    if i % 3 == 0:
        total += i
        count += 1
        print(i)
# Print the total and how many numbers were added.
print("Total of Multiples of 3:", total)
print("Numbers added:", count)


#========================10.Even vs Odd Counter============================
#Use two counters inside the same loop.
#1.  Take N from the user.
n=int(input("Enter a number: "))
even_num=0
odd_num=0
#2.  Loop from 1 to N.
for i in range(1, n + 1):
#3.  Count how many values are even and how many are odd.
    if i%2==0:
        even_num=even_num+1
    else:
        odd_num=odd_num+1
#4.  Print both counts after the loop.
print("Even Number:", even_num)
print("Odd Number:", odd_num)