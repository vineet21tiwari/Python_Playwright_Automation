

#1 Student Exam Eligibility
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

# 5Online Store Discount Access
# OR
# IF-ELSE
# DISCOUNT
# A shopper receives a 10 %discount
# if the order is large enough or if they are a premium member
# Take order amount.Take premium-member status as yes or no.

Order_amount = float(input("Enter Order Amount: "))
Customers_status = input("Enter if Customer is  Premium Member: ")
if Customers_status == "Yes" or Order_amount > 10000:
    print("Customer is Premium Member")
    finel_cost = (Order_amount - Order_amount*0.15)
else: finel_cost = (Order_amount - Order_amount*0.10)

# 6 Emergency Entry Permission
# OR
# ==
# IF-ELSE
# A restricted facility normally requires an access card, but emergency staff are also allowed entry.
# 1.
# 2.
# 3.
# 4.
# 5.
# Take whether the person has a valid access card.
# Take the person's role: employee, doctor, firefighter or visitor.
# Allow entry if the access card is valid or role is doctor or firefighter.
# Otherwise print Entry denied.
# Print the exact reason for the granted access in a separate message

isit_valid_access_card = input("Enter if the person have valid access card: "))
person_role = input("Enter persons role entering hospital: "))
if isit_valid_access_card == "Yes" or person_role =="doctor" or person_role =="firefighter":
    print("Allow entry into yhe building")
if  isit_valid_access_card == "Yes":
    print(" entry granted because of valid access card")
# 7 Free Delivery Rule
# OR
# AND
# IF-ELIF-ELSE
# An e-commerce app decides whether delivery is free, discounted or charged normally.
# 1.
# 2.
# 3.
# 4.
# 5.
# Questions 07-08
# Take cart value and membership status.
# Give free delivery if cart value is at least 999 or the user is a premium member.
# If cart value is between 499 and 998 and the user is not premium, charge a reduced delivery fee of 40.
# Otherwise charge a normal delivery fee of 80.
# Print cart value, delivery fee and final payable amount

order_amount = int(input("Enter cart value: "))
member_status_premium = input("Enter member premium status: ")
if member_status == "Yes" or  order_amount >= 999:
   print("No Dejivery fee is Charged")
elif member_status != "Yes" or ( order_amount >= 499 and order_amount < 999):
    print(" Dejivery fee of $40 is Charged")
else: print( "Dejivery fee of #80 is Charged")


#8 Sports Team Selection
# OR
# AND
# IF-ELIF
# A student can qualify for the sports team through performance in either speed or endurance, provided attendance
# is acceptable.
# 1.
# 2.
# 3.
# 4.
# 5.
# Take 100-metre race time, endurance score and attendance percentage.
# Qualify if race time is 14 seconds or less or endurance score is at least 80.
# Additionally, attendance must be at least 75.
# If sporting criteria pass but attendance fails, print Performance qualified - attendance insufficient.
# Otherwise print selected/not selected appropriately


race_time = int(input("Enter Race Time for 100- meter race: "))
endurance = int(input("Enter endurance achieved value: "))

attendance_achieved  = int(input("Enter member Attendance achieved: "))
if (race_time <= 14 or  endurance <= 80) and attendance_achieved <= 75:
   print("Thid student is qualified for the sports team")
elif member_status != "Yes" or ( order_amount >= 499 and order_amount < 999):
    print(" Dejivery fee of $40 is Charged")
else: print( "Dejivery fee of #80 is Charged")

#9  Blocked Account Access
# NOT
# AND
# BOOLEAN
# A user may access an application only if the password is correct and the account is not blocked.
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# Store the correct password in a variable.
# Take the user's password.
# Take blocked status as
# True or
# False in the program.
# Allow access when the password matches and
# not is_blocked .
# If password is correct but the account is blocked, print Contact support.
# Otherwise print Incorrect password
username='usmanji'
userpin=7151
Employee_loginid = input("Enter employee Userid: ")
Employee_pin = int(input("Enter employee PIN: "))
Employee_isactive = input("Enter if employee is active: ")
if Employee_loginid == username and  Employee_pin == userpin:
    print("Employee login is successful")
else:
    print("Employee login is not successful")
if Employee_isactive != true:
    print("Employee account is not Active")

# 10     Library Book Issue Check
# NOT
# AND
# IF-ELSE
# A library issues a book only when the member is active and does not have an overdue book.
# 1.
# 2.
# 3.
# 4.
# 5.
# Take member-active status and overdue-book status.
# Issue the book if member is active and the user does not have an overdue book.
# If membership is inactive, print Renew membership first.
# If membership is active but overdue exists, print Return overdue book first.
# Use
# not explicitly in at least one condition

username = 'usmanji'
userpin = 7151
Employee_loginid = input("Enter employee Userid: ")
Employee_pin = int(input("Enter employee PIN: "))
Employee_isactive = input("Enter if employee is active: ")
if Employee_loginid == username and Employee_pin == userpin:
    print("Employee login is successful")
else:
    print("Employee login is not successful")
if Employee_isactive != true:
    print("Employee account is not Active")

#11  Movie Ticket Age Rule
# AND
# OR
# PARENTHESES
# A cinema allows entry to an age-restricted movie under two possible paths.
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# Take age, whether the person has valid ID, and whether a guardian is present.
# Allow normal entry when age is at least 18 and valid ID is available.
# Also allow a 16-17 year old when a guardian is present.
# Use parentheses to combine the two valid paths clearly.
# Print Entry allowed or Entry denied.
# Add a special message when age is below 16


race_time = int(input("Enter Race Time for 100- meter race: "))
endurance = int(input("Enter endurance achieved value: "))

attendance_achieved = int(input("Enter member Attendance achieved: "))
if (race_time <= 14 or endurance <= 80) and attendance_achieved <= 75:
    print("Thid student is qualified for the sports team")
elif member_status != "Yes" or (order_amount >= 499 and order_amount < 999):
    print(" Dejivery fee of $40 is Charged")
else:
    print("Dejivery fee of #80 is Charged")

#12 Employee Work-from-Home Eligibility
# AND
# OR
# NOT
# IF-ELIF
# A company allows work from home based on role, performance and security restrictions.
# 1.
# 2.
# 3.
# 4.
# 5.
# Questions 11-12
# Take employee role, performance rating and whether the employee is under a security restriction.
# Allow WFH when role is developer or analyst, performance rating is at least 3, and the employee is not
# restricted.
# If role and performance qualify but restriction is active, print WFH blocked by security restriction.
# Otherwise print WFH not eligible.
# Use parentheses around the role alternatives


race_time = int(input("Enter Race Time for 100- meter race: "))
endurance = int(input("Enter endurance achieved value: "))

attendance_achieved = int(input("Enter member Attendance achieved: "))
if (race_time <= 14 or endurance <= 80) and attendance_achieved <= 75:
    print("Thid student is qualified for the sports team")
elif member_status != "Yes" or (order_amount >= 499 and order_amount < 999):
    print(" Dejivery fee of $40 is Charged")
else:
    print("Dejivery fee of #80 is Charged")

# 13 Hospital Appointment Priority
# AND
# OR
# IF-ELIF-ELSE
# A clinic assigns priority based on age, temperature and emergency status.
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# Take patient age, temperature and emergency status.
# Assign High Priority if emergency is yes or temperature is 103 or above.
# Assign Priority if age is 65 or above and temperature is at least 100.
# Otherwise assign Normal Queue.
# Print all patient details and the assigned category.
# Ensure the high-priority rule is checked before the lower-priority rule

race_time = int(input("Enter Race Time for 100- meter race: "))
endurance = int(input("Enter endurance achieved value: "))

attendance_achieved = int(input("Enter member Attendance achieved: "))
if (race_time <= 14 or endurance <= 80) and attendance_achieved <= 75:
    print("Thid student is qualified for the sports team")
elif member_status != "Yes" or (order_amount >= 499 and order_amount < 999):
    print(" Dejivery fee of $40 is Charged")
else:
    print("Dejivery fee of #80 is Charged")
# 14 Scholarship Decision System
# AND
# OR
# ELIF
# PERCENTAGE
# A scholarship program evaluates academic performance, family income and sports achievement.
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# Take three subject marks and calculate percentage.
# Take annual family income and sports-achievement status.
# Give Full Scholarship if percentage is at least 90 and family income is at most 500,000.
# Give Merit Scholarship if percentage is at least 85 or sports achievement is yes.
# Otherwise print Not eligible for scholarship.
# Print percentage rounded to 2 decimal places along with the final decision.


race_time = int(input("Enter Race Time for 100- meter race: "))
endurance = int(input("Enter endurance achieved value: "))

attendance_achieved = int(input("Enter member Attendance achieved: "))
if (race_time <= 14 or endurance <= 80) and attendance_achieved <= 75:
    print("Thid student is qualified for the sports team")
elif member_status != "Yes" or (order_amount >= 499 and order_amount < 999):
    print(" Dejivery fee of $40 is Charged")
else:
    print("Dejivery fee of #80 is Charged")

#15 Airport Boarding Eligibility System
# AND
# OR
# NOT
# IF-ELIF-ELSE
# MASTER
# Question 15
# Build a simplified airport boarding checker that combines identity, ticket, baggage and special-assistance rules.
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# Take passenger name, age, ticket status, valid-ID status, baggage weight and special-assistance status.
# A normal adult passenger may board only when ticket is valid and ID is valid and baggage is at most 20 kg.
# A passenger below 18 may board when ticket is valid and a guardian is present.
# If baggage exceeds 20 kg but all other normal-adult requirements pass, print Pay excess baggage fee before
# boarding.
# If ticket is not valid, deny boarding regardless of other values.
# If special assistance is requested and boarding is otherwise allowed, print an additional assistance message.
# Use at least one
# and , one
# or and one


race_time = int(input("Enter Race Time for 100- meter race: "))
endurance = int(input("Enter endurance achieved value: "))

attendance_achieved = int(input("Enter member Attendance achieved: "))
if (race_time <= 14 or endurance <= 80) and attendance_achieved <= 75:
    print("Thid student is qualified for the sports team")
elif member_status != "Yes" or (order_amount >= 499 and order_amount < 999):
    print(" Dejivery fee of $40 is Charged")
else:
    print("Dejivery fee of #80 is Charged")

e_mail = input("Enter a emailr : "))
if '@' in e_mail and '.' in e_mail:
    then print("That email is valid")
else: print("That email is not valid")

course_tojoin = input("Enter course to join: ")
course_available = ['c','c++','python','java','sql']
if course_tojoin in course_available:
    print("That course is available")
else: print("That course is not available")


student_subjects=input("Enter student subject: ")
student_marks=input("Enter student marks in subject: ")
subjects_available = ['math','english','science',]
student_attendence_percent= input("Enter student attendance percentage: ")

if student_subjects in subjects_available: and student_marks>=40 and student_attendence_percent>=75:
  print("That subject is available and student is passed")
else: print("That subject is not eligible")