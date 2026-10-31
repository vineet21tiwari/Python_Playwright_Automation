

# Student Exam Eligibility
# AND
# IF-ELSE
# AVERAGE
# Questions 01-02
# A school allows a student to pass only when academic performance
# and attendance are both acceptable.
#
# Take marks in Maths, Science and English and calculate the average.
# Take attendance percentage.
# If average is at least 40 and attendance is at least 75, print PASS - Eligible.
# Otherwise print Not Eligible.
# Also print total marks, rounded average and attendance.
# Add an
# elif : if average is at least 40 but attendance is below 75
# , print Academically passed, attendance
# shortage.\

Math_marks = int(input("Enter Math Marks: "))
Science_marks = int(input("Enter Science Marks: "))
English_marks = int(input("Enter English Marks: "))
Attendance_percent = int(input("Enter Attendance Percentage: "))
Average_marks = (Math_marks + Science_marks + English_marks)//3
if Average_marks >= 40 and Attendance_percent >= 75:
    print("Passed and Eligible.")
else: print("Not Eligible.")
if Average_marks >= 40 and Attendance_percent < 75:
    print("Academically Passed but Attendance Shortage so Not Eligible.")
#
# 2 Loan Pre-Eligibility Checker
# AND
# IF-ELIF-ELSE
# A bank performs a simple preliminary eligibility check before processing a loan application.
# 1.
# 2.
# 3.
# 4.
# 5.
# Take applicant age, monthly salary and credit score.
# Approve the preliminary check only if age is at least 21, salary is at least 30,000 and credit score is at least 700.
# If age and salary qualify but credit score is below 700, print Credit score needs improvement.
# Otherwise print Not eligible for preliminary check.
# Print all three entered values in the final summary.
# Assignment 04 - Logical Operators

applicant_age = int(input("Enter applicant age: "))
Monthly_salary = float(input("Enter monthly salary: "))
Credit_score = int(input("Enter credit score: "))
if (applicant_age >= 21
        and Monthly_salary >= 30000 and Credit_score >= 700):
    print("Preliminary check approved.")
elif applicant_age >= 21 and Monthly_salary >= 30000 and Credit_score < 700:
    print("Credit score needs improvement.")
else:
    print("Not eligible for preliminary check.")
    print(applicant_age)
    print(Monthly_salary)
    print(Credit_score)
#
# 3 Secure Office Login
# AND
# ==
# IF-ELSE
# An employee can enter a secure dashboard only when both username
# and PIN are correct.
# Store a correct username and correct PIN in variables.
# Take username and PIN from the user.
# If both match, print Login successful.
# Otherwise print Invalid credentials.
# Add a second condition requiring
# account_active == True .
# If credentials are correct but the account is inactive,
# print a separate message using

username='usmanji'
userpin=7151
Employee_loginid = input("Enter employee Userid: ")
Employee_pin = int(input("Enter employee PIN: "))
Employee_isactive = input("Enter if employee is active: ")
if Employee_loginid == username and  Employee_pin == userpin:
    print("Employee login is successful")
else:
    print("Employee login is not successful")
if Employee_isactive != True:
    print("Employee account is not Active")
# 4
# Theme# Park# Ride# Safety# Check# AND# RANGE# IF - ELSE
# A# ride is allowed# only# when# the# visitor# meets
# both# age and height# requirements
# Take# visitor# age and height in centimetres.# Allow# the
# ride# only# when# age is at# least# 12 and height is at
# least# 140# cm.# If# age# qualifies# but# height
# does# not, print# Height# requirement# not met.
# If# height# qualifies# but# age# does
# not, print# Age# requirement# not met.
# Otherwise# print# Ride# allowed
# only# for the fully valid case

Visitors_age = int(input("Enter Visitors age: "))
Visitors_Hight = float(input("Enter Visitors Hight: "))
Credit_score = int(input("Enter credit score: "))
if (Visitors_age >= 12
        and Visitors_Hight >= 140):
    print("Preliminary check approved")
elif (Visitors_age < 12 and Visitors_Hight >= 140):
    print("Age requirement not Met")
elif (Visitors_age > 12 and Visitors_Hight < 140):
    print("Hight requirement not Met")
else: print("Ride# allowed only for the fully valid case Visitors")

#Online Store Discount Access
#OR
#IF-ELSE
#DISCOUNT
#A shopper receives a 10 %discount
#if the order is large enough or if they are a premium member
#Take order amount.Take premium-member status as yes or no.

Order_amount = float(input("Enter Order Amount: "))
Customers_status = input("Enter if Customer is  Premium Member: "))
if Customers_status == "Yes" or Order_amount > 10000:
    print("Customer is Premium Member")
    finel_cost = (Order_amount - Order_amount*0.15)
else finel_cost = (Order_amount - Order_amount*0.10)

