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


#==========================11.Divisibility Counter Challenge=====================
#Count values that satisfy one condition and a more specific second condition.
#1.  Loop from 1 to 100.
count_divisible_by_5 = 0
count_divisible_by_5_not_10 = 0

for i in range(1, 101):
    if i % 5 == 0:
        count_divisible_by_5 += 1

    if i % 5 == 0 and i % 10 != 0:
        count_divisible_by_5_not_10 += 1

print("Numbers divisible by 5:", count_divisible_by_5)
print("Numbers divisible by 5 but not 10:", count_divisible_by_5_not_10)

#2.  Count how many numbers are divisible by 5.
#3.  Separately count how many are divisible by 5 but not divisible by 10.
#4.  Print both counts




#==================12.Five-Student Marks Analyzer====================
#Collect repeated user input without using a list.
#1.  Run the loop exactly 5 times.
total_marks=0
pass_count=0
fail_count=0
for i in range(1,6):
    marks=int(input("Enter marks: "))
    total_marks += marks
#2.  Inside the loop, take one student mark from the user.
    if marks>=40:
        print("Pass")
        pass_count+=1
    else:
        print("Fail")
        fail_count+=1
#3.  Maintain total marks, pass count (marks >= 40) and fail count.

print("Total Marks for Student:", total_marks)
print("Pass Count is 40", pass_count)
print("Fail Count is 40", fail_count)

#4.  After the loop, calculate and print the average, pass count and fail count.
average= total_marks/5
#5.  Round the average to 2 decimal places.
print("Average is", round(average,2))


# ========================13.Multiplication Table==================
# Generate a complete table from one user input.
# 1.  Take a number from the user.
num = int(input("Enter a number: "))
# 2.  Print its multiplication table from 1 to 10.
count = 1
while count < 11:
    final_num =num * count
# 3.  Format each line like 7 x 3 = 21.
    print(num, "X", count, "=", final_num)
    count += 1

#======14.Three / Five / ThreeFive==================
#Practice condition ordering inside a loop.
#1.  Loop from 1 to 50.
num=1
for num in range(1,51):
#2.  If a number is divisible by both 3 and 5, print ThreeFive.
    if num %3 ==0 and num%5==0:
        print("Number is divisible by 3 and 5:", num)
#3.  Else if divisible by only 3, print Three.
    elif num %3 == 0 and num%5 != 0:
        print("Number is divisible by 3 :", num)
#4.  Else if divisible by only 5, print Five.
    elif num %3 != 0 and num%5 == 0:
        print("Number is divisible by 5 :", num)
    else:
#5.  Otherwise print the number itself.
        print("Number is not divisible by 3 & 5 :", num)


#==============15.Vowel Explorer======================
#Iterate through a string and reuse the membership operator.
#1.  Take one word from the user and convert it to lowercase.
word=input("Enter a word: ").lower()
count=0
vowel_count=0
#2.  Loop through every character.
while count < len(word):
#3.  If the character is in aeiou, print the vowel and increase a vowel counter.
    if word[count] in "a" or word[count] in "e" or word[count] in "i" or word[count] in "o" or word[count] in "u":
        print(word[count])
        vowel_count+=1
    count+=1

#4.  Print the total number of vowels after the loop.
print("Vowel Count:",vowel_count)


#===================16.Five-Product Shopping Summary=================
# Use repeated input to produce a small shopping report without lists.
#1.  Run a loop 5 times and take one product price each time.
total_cost=0
count=0
for i in range(1,6):
# 2.  Calculate the total cost of all 5 products.
    product_price=int(input("Enter product price: "))
    total_cost+=product_price
#3.  Count how many products cost more than 1000.
    if product_price>1000:
        count += 1
#4.  Calculate the average product price.
average_price=total_cost/5
#5.  Print total, average and expensive-product count
print("Average cost:", average_price)
print("Total cost:",total_cost)
print("Expensive products count:",count)

#=================17.Student Eligibility Batch======================
#Apply the same eligibility rule to several students.
#1.  Process exactly 5 students.
eligible_count=0
not_eligible_count=0
for i in range(1,6):
#2.  For each student, take marks and attendance percentage.
    marks=int(input("Enter marks: "))
    attendance_percentage=int(input("Enter attendance percentage: "))
#3.  A student is eligible when marks >= 40 and attendance >= 75.
    if marks >=40 and attendance_percentage>=75:
#4.  Print Eligible / Not Eligible for each student.
        print("student is Eligible")
        eligible_count+=1
    else:
        print("student is Not Eligible")
        not_eligible_count+=1
#5.  At the end print total eligible and not-eligible counts
print(eligible_count)
print(not_eligible_count)


#================18. Selective Range Challenge================

num = int(input("Enter N: "))
count = 0
total = 0

# 1. Loop from 1 to N
for i in range(1, num + 1):

    # 2. Select numbers divisible by 3 or 5, but not both
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):

        # 3. Print every selected number
        print(i)

        # 4. Count selected numbers and calculate their sum
        count += 1
        total += i

# 5. Print final count and sum
print("Total count:", count)
print("Total sum:", total)

#=======================19 while Warm-Up: 1 to 10==================================
#Rewrite a basic counted loop using while.
#1.  Start a variable at 1.
num=1
#2.  Use a while loop to print 1 through 10.
while num<=10:
    print(num)
    #3.  Increase the variable correctly so the loop ends
    num+=1

#======================20.Countdown with while==================
#.  Start at 10.
number=10
#2.Print 10 down to 1 using while.
while number>0:
#3.  Decrease the variable by 1 each iteration.
    print(number)
    number-=1
#.  After the loop, print Go!.
print("GO!")

#============================21.Sum 1 to N Using while================================
# 1.  Take N from the user.
number = int(input("Enter a number: "))
count = 0
total = 0
# 2.  Use while to calculate the sum from 1 to N.
while count < number:
    # 3.  Maintain both a counter variable and a total variable
    count += 1
    total += count

# 4.  Print the final total
print(total)


#===============22 Multiplication Table with while==================

#1.  Take a number from the user.
num=int(input("Enter a Number:"))
count=1
#2.  Use while to print its table from 1 to 10.
while count<=10:
   total=num * count
   print(num, "X", count, "=", total)
#3.  Format the output like 6 x 4 = 24
   count += 1


#=================23.Even Numbers with while==================
#1.   Print   all   even   numbers   from  2   to   50   using   while .
count=2
while count <=50:
    count % 2==0
# 2.  Start at 2 and increase by 2 each iteration.
    print(count)
    count+=2


#================24.Password Until Correct=================
# 1. Set the correct password to python123.
password = "python123"

# 2.  Ask the user for a password before entering the loop.
userPwd = input("Enter user password: ")
while password != userPwd:
    print("Incorrect password")
    userPwd = input("Try again: ")
print(" Login Successful.")



#====================25.ATM PIN - Maximum 3 Attempts=====================
#1.  Set a correct PIN, for example 4321.
correct_pin = 4321
count = 1

pin = int(input("Enter your PIN: "))

#3.  Continue while attempts are below 3 and the PIN is incorrect.
while pin != correct_pin and count < 3:
    print("Incorrect PIN")
    pin = int(input("Try Again: "))
    count += 1
#4.  After the loop, print Access Granted if correct; otherwise print Card Blocked.
if pin == correct_pin:
    print("Access Granted")
else:
    print("Card Blocked.")

#===================26.Shopping Total Until 0=======================
#1.  Ask the user to enter a product price.
productPrice=float(input("Enter product price: "))
#2.  Keep accepting prices while the entered price is not 0.
total=0
count=0
average_price=0
#3.  Add every non-zero price to a running total and count the number of products.
while productPrice>0:
    total+=productPrice
    count+=1
    productPrice = float(input("Enter product price: "))

#5.  Print the number of products, total amount and average price.
print(count)
print(total)
if count>0:
    average_price= total/count
    print(average_price)
else:
    print("No Products Found")
#4.  When the user enters 0, stop the loop.
#6.  Handle the case where the first entered value is 0 without dividing by zero
