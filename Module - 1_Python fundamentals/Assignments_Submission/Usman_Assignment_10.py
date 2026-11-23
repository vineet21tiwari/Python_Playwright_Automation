# # QUESTION 1:Create marks = [78, 45, 91, 62, 38, 85] and print
# the complete list.
# Calculate and print total marks and class average.
# Count how many students passed using 40 as the passing mark.
# Print the highest and lowest marks
# from html.parser import interesting_normal

marks = [78, 45, 91, 62, 38, 85]
print(marks)
print(sum(marks),sum(marks)/len(marks))
no_of_stdnts_passed=0
for mark in marks:
    if mark > 40:
        no_of_stdnts_passed += 1
print(no_of_stdnts_passed)

## QUESTION 2: Start with cart = ["Laptop", "Mouse", "Keyboard"].
# Remove "Mouse" by value.
# Add "Monitor" at the end and insert "USB Hub" at index 1.
# Remove the last item using pop() and store the removed item in a variable.
# Print the removed item, final cart and total number of items

cart = ["Laptop", "Mouse", "Keyboard"]
cart.remove('Mouse')
print(cart)
cart.append('Monitor')
cart.insert(1,'USB Hub')
print(cart)
cart.pop()
print(cart)
last_removed_item=cart.pop()
print(cart,'total number of items',len(cart))
print(last_removed_item)

# QUESTION 3:Use sales = [1200, 950, 1800, 1500, 2100, 1750, 1300]
# Print every second value and then print the
# complete list in reverse using slicing.
# Sort the sales in ascending order and print them.
# Sort the same list in descending order and print the result

sales = [1200, 950, 1800, 1500, 2100, 1750, 1300]
print(sales[0::2])
print(sales[::-1])
print(sorted(sales.copy(),reverse=True))

# QUESTION 4:Use numbers = [12, -5, 7, 20, -8, 15, 0, 18]
# Loop through the list and skip negative values using continue.
# Count positive numbers and negative numbers separately.
# Count even and odd values; do not count zero as odd.
# Create a new list containing only positive even numbers
positivcnt = 0
negetivcnt = 0
evencnt = 0
oddcnt = 0
new_numbers =[]
numbers = [12, -5, 7, 20, -8, 15, 0, 18]
for number in numbers:
    if number>0 and number%2==0:
        new_numbers.append(number)
    if number > 0 or number!=0:
        positivcnt+=1

        if number>0 and number%2==0:
            evencnt+=1

        elif number>0 and number%2!=0:
            oddcnt+=1

        elif number<0:
            negetivcnt+=1
    else:
        continue
print('number of Even Numbers:',evencnt, end='')
print('number,of Odd Numbers:',oddcnt, end='')
print('number of Positive numbers are:',positivcnt, end='')
print('Number of Negetive Numbers:',negetivcnt)
print('Number of Positive even numbers are:',new_numbers)

# QUESTION 5: Start with users = ["aman", "priya", "rahul", "aman"]
# Print how many entries are currently stored, including duplicates.
# Create a new empty list and remove duplicates manually
# using a loop and membership check.
# Take one new username from the user and add it only if it is
# not already present.
# Sort and print the final username list

users = ["aman", "priya", "rahul", "aman"]
non_doop_users=set(users)
print(len(users))
users.append("rahul")
new_user=input(print('Enter a user name:'))
if new_user not in non_doop_users:
    users.append(new_user)
print(users)
print(non_doop_users)
print(sorted(users))

# QUESTION 6:Create courses = ("Python", "Playwright", "SQL", "Git", "API").
# Print the first three courses using slicing.
# Print the tuple in reverse using slicing.
# Print the total number of courses using len()

courses = ("Python", "Playwright", "SQL", "Git", "API")
print(courses[0:3:])
print(courses[::-1])
print(len(courses))
# QUESTION 7:Use marks = (76, 88, 65, 92, 54)
# Loop through the tuple and print every mark.
# Calculate the total and average marks.
# Count how many marks are at least 75.
# Print the highest and lowest values

marks = (76, 88, 65, 92, 54)
total = sum(marks)
loop_total = 0
avg   =0
cnt =0
for mark in marks:
    print(mark,end='')
    loop_total += mark
    if mark > 70:
        cnt+=1
avg = loop_total/len(marks)
nrm_avg= total/len(marks)
print('Average using function:',avg,'Average using loop logic:',nrm_avg)
print('Number of marks more than 70:',cnt)
print('Highest and Lowest marks in tupple is :',max(marks),min(marks))

# QUESTION 8:Use codes = (200, 404, 200, 500, 200, 404).
# Count how many times 200 occurs.
# Find the first index of 404.
# Check whether 401 exists in the tuple.
# Print all unique code values by converting
# the tuple to a set for display only


codes = (200, 404, 200, 500, 200, 404)
unq_codes=set(codes)
cnt = 0
for code in codes:
    if code == 200:
        cnt += 1
    if code == 404:
        print(codes.index(404))
    if code == 401:
        print(unq_codes,end='')
print(cnt)
print(unq_codes)

# QUESTION 9:
# Create employee = ("Aman", "QA", 55000, True)
# Unpack the tuple into four separate variables.
# Print each unpacked value with a clear label.
# Print the data type of the original employee variable.
# Explain in a comment why changing employee[1] directly is not allowed.

employee = ("Aman", "QA", 55000, True)
(name,role,salary,result) = employee
print('Employee Name:',name)
print('Employee Role:',role)
print('Employee Salary:',salary)
print('Employee Result pass:',result)

# QUESTION 10:Create a = ("Python") and print its type.
# Create b = ("Python",) and print its type.
# Print both values and compare their types.
# Create a three-value tuple and try to access each element using indexing.
# Write one comment explaining the purpose of the comma
# in a one-item tuple

a = type("Python")
b = type("Python",)
print(a,b,sep='\n')
values=('apple','banana','grape')
print(values[0],values[1],values[2])

# QUESTION 11:Print total registration entries from the list.
# Use students = ["Aman", "Priya", "Aman", "Rahul", "Priya", "Neha"].
# Convert the list into a set and print the unique students.
# Print the number of unique students.
# Add "Rohit" to the set and check whether "Priya" is present.

students = ["Aman", "Priya", "Aman", "Rahul", "Priya", "Neha"]
unq_students = set(students)
print(unq_students,'Number of unique Students is:',len(unq_students))
unq_students.add('Rohit')
print(unq_students)

# QUESTION 12:Start with skills = {"Java", "Python", "SQL"}
# Add "AWS" using add().
# Add "Docker" and "Git" together using update().
# Remove "SQL" safely using discard().
# Print the final set and its size

skills = {"Java", "Python", "SQL"}
skills.add('AWS')
print(skills)
skills.update('Docker') # Need to discuss with vineeth. why it split every letter to add to set?
skills.update('Git')
print(skills)
skills.remove('SQL')
print(skills,len(skills))

# QUESTION 13: Use python_class = {"Aman", "Rahul", "Priya", "Neha"} and playwright_class =
# {"Rahul", "Priya", "Karan"}.
# Print students who attended both classes.
# Print students who attended only Python.
# Print students who attended only Playwright

python_class = {"Aman", "Rahul", "Priya", "Neha"}
playwright_class = {"Rahul", "Priya", "Karan"}

print('Students attending both classes:',python_class.intersection(playwright_class))
print('students who attended only Python:',python_class.difference(playwright_class))
print('students who attended only Playwright:',playwright_class.difference(python_class))

# QUESTION 14: Use coding = {"Aman", "Rahul", "Priya", "Neha"} and robotics = {"Rahul",
# "Karan", "Priya", "Rohit"}.
# Print students who belong to exactly
# one club using symmetric difference.
# Check whether "Neha" belongs to Robotics Club.
# If not, add "Neha" to Robotics Club.
# Print the total number of unique students across both clubs

coding = {"Aman", "Rahul", "Priya", "Neha"}
robotics = {"Rahul","Karan", "Priya", "Rohit"}
lkng='Neha'
print(' students who belong to exactly one club:',coding.symmetric_difference(robotics))
if lkng in robotics:
    print('Yes Neha is in Robotics:')
else:
    robotics.add('Neha')
print(coding.symmetric_difference(robotics))

# QUESTION 15:Create numbers = {10, 20, 30, 40}
# Remove 20 using remove() and print the set.
# Use discard() to remove 50 even though it does not exist.
# Add 30 again and observe whether a duplicate is created.
# Write a comment explaining
# why discard() is safer when the value may be absent

numbers = {10, 20, 30, 40}
numbers.remove(20)
print(numbers)
numbers.discard(30)
print(numbers)
numbers.add(30)
print(numbers)

# QUESTION 16:Use booked_seats = [12, 15, 18, 12, 20, 15, 25]
# Print the total number of booking entries.
# Convert the list to a set and print unique booked seats.
# Take a seat number from the user and add it only if it is
# not already booked.
# Convert the final set back to a list, sort it and print all booked seats

booked_seats = [12, 15, 18, 12, 20, 15, 25]
print(len(booked_seats))
print(set(booked_seats))
new_booked_seats = []
seat_nbr=int(input(print('please enter a seat number to book:')))
if seat_nbr not in booked_seats:
      booked_seats.append(seat_nbr)
      print(booked_seats)

else:
    for i in booked_seats:
        new_booked_seats.append(i)
    print(sorted(new_booked_seats))

# QUESTION 17:Use skills = ["Java", "Python", "SQL", "Java", "AWS", "Python"].
# Convert to a set and print unique skills and unique count.
# If "Docker" is missing, add it to the set.
# Convert the final set to a sorted list and print it

skills = ["Java", "Python", "SQL", "Java", "AWS", "Python"]
st_skils= set(skills)
print(st_skils,len(st_skils))
if 'Docker' not in st_skils:
    st_skils.add('Docker')
    print(sorted(st_skils),len(st_skils))

# QUESTION 18:Use day1 = ["Aman", "Priya", "Rahul", "Aman"] and day2 = ["Rahul", "Neha",
# "Priya", "Rohit"].
# Print attendees who came on at least one day.
# Print attendees who came on both days.
# Convert the common attendees to a sorted list and print it

day1 = ["Aman", "Priya", "Rahul", "Aman"]
day2 = ["Rahul", "Neha","Priya", "Rohit"]
day1.extend(day2)
attendees1 = day1.copy()
print(attendees1,len(attendees1))
attendees2 =set(attendees1)
print(attendees2,len(attendees2))
common_attendees= set(day1).intersection(set(day2))
print(common_attendees,len(common_attendees))

# QUESTION 19:Use
# warehouse_a = [101, 102, 103, 101, 104] and
# warehouse_b = [103, 104, 105, 106, 105].
# Print codes available in both warehouses.
# Print codes available only in Warehouse A.
# Create a sorted list containing all unique item
# codes from both warehouses

warehouse_a = [101, 102, 103, 101, 104]
warehouse_b = [103, 104, 105, 106, 105]
codes_in_both = set(warehouse_a).intersection(set(warehouse_b))
print('codes present in both warehouses:',codes_in_both)
Codes_only_a=set(warehouse_a).difference(warehouse_b)
print(Codes_only_a,len(Codes_only_a))
all_codes=set(warehouse_a).union(warehouse_b)
print(sorted(all_codes),len(all_codes))

# QUESTION 20:Use python = ["Aman", "Priya", "Rahul", "Aman"] and sql = ["Priya", "Karan",
# "Rahul", "Neha"].
# Print students enrolled in both courses.
# Print students enrolled only in Python.
# Print total unique students across the two courses

python = ["Aman", "Priya", "Rahul", "Aman"]
sql = ["Priya", "Karan", "Rahul", "Neha"]
both_courses=python + sql
print(both_courses)
enrolld_both= set(python).intersection(set(sql))
print(enrolld_both)
ebrolld_only_python=set(python).difference(sql)
print(ebrolld_only_python)
print('total unique students across the two courses:',set(python).union(set(sql)))
print(sorted(set(both_courses)),len(sorted(set(both_courses))))