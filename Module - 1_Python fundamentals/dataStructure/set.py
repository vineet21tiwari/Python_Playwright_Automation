# A set stores mulyiple values,
# but it keeps only unique values nd does not gurantee a fixed order

# List ---- > [], list = [] , to add elements  ---> append()
# tuple ---> (), tuple = () : no sense of creating empty tuple
# set -----> { },  fruits = { } : no it is for dictionary, to add elements ---> add()

fruits = {"apple", "banana", "cherry", "banana"}
print( "mango" in fruits)
print(fruits)

numbers = set()
numbers2 = {}

print(type(numbers))
print(type(numbers2))

# how many unique elements are present in this list
list = [10,20,30,20,30,50, 70,40, 80, 50,20]
print(list)
numbers = set(list)
# for num in list:
#     numbers.add(num)

print(numbers)
print("Unique elements ",len(numbers))

# A training institute receives this registration list:
students = [
    "Aman",
    "Rahul",
    "Priya",
    "Aman",
    "Neha",
    "Rahul",
    "Karan"
]
# Complete these tasks:
# a. Print the total number of registrations.
# b. Convert the list into a set and print only unique students.
# c. Print how many unique students registered.
# d. Check whether "Priya" is registered.
# e. Add "Rohit" to the unique student set and print the final set.
# print(len(students))
# unique_students = set(students)
# print(set(students))
# print(len(set(students)))
# if "priya" in students:
#     print("Priya is registered")
# unique_students.add("Rohit")

# Two Classroom Attendance Analyzer
# Two trainers recorded attendance:
python_class = {"Aman", "Rahul", "Priya", "Neha", "Karan"}
playwright_class = {"Rahul", "Priya", "Rohit", "Karan"}
#
# Complete these tasks:
# a. Print all students who attended at least one class.
print("all students registered", python_class | playwright_class)
# b. Print students who attended both classes.
print("both classes ", python_class & playwright_class)

# c. Print students who attended Python only.

print("python only ", python_class - playwright_class)
# d. Print students who attended Playwright only.

print("playwright only", playwright_class - python_class)
# e. Print the total number of unique students across both classes.
print("total unique students", len(python_class | playwright_class))
# set 1 union set 2 = unique elements on both , operator:  |
# set 1 intersectionn set 2  =  common el;ements on nboth sets, operator : &
# set 1 difference set 2 = elements presetn on ony set 1, operator : -
# set2 differnce set 1 = elements present on set 2 only

