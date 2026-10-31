# ==========1 Student Exam Eligibility AND IF-ELSE AVERAGE ===============
#A school allows a student to pass only when academic performance and attendance are both acceptable.
#Take marks in Maths, Science and English and calculate the average.
math_marks = int(input("Enter math marks: "))
science_Marks = int(input('Enter science marks: '))
english_Marks = int(input("Enter english marks: "))
#Take attendance percentage.
attendance_percentage = float(input("Enter attendance percentage: "))
total_marks = math_marks + science_Marks + english_Marks
average_marks = total_marks / 3

#If average is at least 40 and attendance is at least 75, print PASS - Eligible.
if average_marks >=40 and attendance_percentage >=75:
    print("Student is PASS-Eligible")

#Add an elif : if average is at least 40 but attendance is below 75, print Academically passed, attendance shortage.
elif average_marks ==40 and attendance_percentage<75:
    print("Student is Academically passed, attendance shortage")
 #   Otherwise print Not Eligible.
else:
    print("Student is FAIL-Eligible")
#Also print total marks, rounded average and attendance.
print("Total Marks:", total_marks)
print("Average Marks:", round(average_marks,3))
print("Student Attendance Percentage:",attendance_percentage)

#======================2. Loan Pre-Eligibility Checker AND IF-ELIF-ELSE ======================
#A bank performs a simple preliminary eligibility check before processing a loan application.
#1.Take applicant age, monthly salary and credit score.
age = int(input("Enter age:"))
monthly_salary = float(input("Enter salary:"))
credit_score = int(input("Enter credit score:"))
#2.Approve the preliminary check only if age is at least 21, salary is at least 30,000 and credit score is at least 700.
if age >= 21 and monthly_salary >=30000 and credit_score >=700:
    print("Preliminary check is Approved")
#3.If age and salary qualify but credit score is below 700, print Credit score needs improvement.
elif age < 21 and monthly_salary <30000 and credit_score < 700:
    print("Credit score needs improvement")
# 4. Otherwise print Not eligible for preliminary check.
else:
    print("Not eligible for preliminary check")
#5.Print all three entered values in the final summary
    print("Age of the Person:" ,age)
    print("Monthly Salary:" ,monthly_salary)
    print("Credit Score:" ,credit_score)

#=====================3. Secure Office Login AND IF-ELSE =========================
# An employee can enter a secure dashboard only when both username and PIN are correct.
# 1.Store a correct username and correct PIN in variables.
#2.Take username and PIN from the user.
username = input("Enter username: ")
pin = input("Enter pin:")
# 3.If both match, print Login successful.
if username == 'mmutyala' and pin == '1234':
     print("Login successful")
     # 4. Otherwise print Invalid credentials.
else:
     print("Login failed")

 # 5.Add a second condition requiring account_active == True .
 account_active = input("Enter account active(True/False): ")
if username == 'mmutyala' and pin == '1234' and account_active == True:
     print("Login successful and account is active")
 # 6.If credentials are correct but the account is inactive, print a separate message using
elif username == 'mmutyala' and pin == '1234' and account_active == False:
     print("Login failed and account is inactive")

 # ####Need to check with vineet for case-sensitive and if account_active value is other than true/False,o/p is not handling correctly


#============4.Theme Park Ride Safety Check=========================
# 1. Take visitor age and height in centimetres.
age= int(input("Enter age: "))
height = int(input("Enter height: "))
# 2. Allow the ride only when age is at least 12 and height is at least 140 cm.
if age >= 12 and height >=140:
    print("You are Eligible")
#3. If age qualifies but height does not, print Height requirement not met.
elif age>=12 and height <140:
    print("Height requirement not met")
#4.If height qualifies but age does not, print Age requirement not met.
elif height > 140 and age <12:
    print("Age requirement not met")
else:
#5. Otherwise print Ride allowed only for the fully valid case.
    print("Ride allowed only for the fully age >=12 and height >=140Cms.")



#====================== 5. Online Store Discount Access======================
# A shopper receives a 10% discount if the order is large enough or if they are a premium member
# 1.Take order amount.
order_amount = float(input("Enter order amount: "))
# 2. Take premium-member status as yes or no .
premium_member_status = input("Enter premium member status(Yes/No): ")
#6. Add an elif : if order amount is at least 10,000 and the member is premium, give 15% instead
if order_amount >= 10000 and premium_member_status == 'Yes':
    print("Customer is premium member and eligible for a 15% discount")
    discount_bill = order_amount * 15 / 100
#3.If order amount is at least 5000 or the customer is premium, apply a 10% discount.
elif (order_amount>=5000 and order_amount<9999) or premium_member_status == 'Yes':
     print("Customer is premium member and eligible for a 10% discount")
     discount_bill = order_amount * 10 / 100
# 4. Otherwise keep the original bill.
elif order_amount <4999 or premium_member_status == 'No':
    discount_bill = 0
    print("You are not Eligibile for any discount")

# 5.Print original bill, discount amount and final bill.
final_bill = order_amount - discount_bill
print("Original Bill for Today:", order_amount)
print("Your discount Amount is:", discount_bill)
print("Your Final Bill for Today:", final_bill)

 #======================  6.Emergency Entry Permission ======================
# A restricted facility normally requires an access card, but emergency staff are also allowed entry.
#1.Take whether the person has a valid access card.
access_card_number= int(input("Enter access card number: "))
#2.Take the person's role: employee, doctor, firefighter or visitor.
employee_Role = input("Enter employee Role(Employee/Doctor/Firefighter/Visitor: ")
#3.Allow entry if the access card is valid or role is doctor or firefighter.
if access_card_number == '12345' or (employee_Role == 'Doctor' or employee_Role == 'Firefighter'):
    print("Employee is Allowed")
#5.Print the exact reason for the granted access in a separate message
    print("Your Role matched for the Entry Access at the moment:",employee_Role)
#4. Otherwise print Entry denied.
else:
    print("You are not Allowed at the Moment")

#======================== 7.Free Delivery Rule===============================
#1.Take cart value and membership status.
cart_value = float(input("Enter cart value: "))
membership_status = input("Enter membership status(Yes/No): ")
#3.If cart value is between 499 and 998 and the user is not premium, charge a reduced delivery fee of 40.
if (cart_value>=499 and cart_value<999) and membership_status == 'Yes':
    delivery_fee=40
#2.Give free delivery if cart value is at least 999 or the user is a premium member.
elif cart_value>=999 or membership_status == 'Yes':
    delivery_fee=0
#4.otherwise charge a normal delivery fee of 80.
else:
    delivery_fee=80
#5.Print cart value, delivery fee and final payable amount.
final_bill = cart_value + delivery_fee
print("Your Total Order for Today:", cart_value)
print("Your Delivery Fee:", delivery_fee)
print("Your Final Bill for Today:", final_bill)

#============================8.Sports Team Selection==============================
#A student can qualify for the sports team through performance in either speed or endurance, provided attendance is acceptable.
#1.Take 100-metre race time, endurance score and attendance percentage.
race_time= int(input("Enter race time: "))
endurance_score = int(input("Enter endurance score: "))
attendance_percentage = int(input("Enter attendance percentage: "))
# 2. Qualify if race time is 14 seconds or less or endurance score is at least 80.
# 3. Additionally, attendance must be at least 75.
if (race_time <= 14 or endurance_score>= 80) and attendance_percentage >=75:
    print("Student is Qualified")
# 4. If sporting criteria pass but attendance fails, print Performance qualified - attendance insufficient.
elif (race_time <=14 or endurance_score>=80) and attendance_percentage <75:
    print("Performance qualified - attendance insufficient")
#5. Otherwise print selected/not selected appropriately.
else:
    print("Student is Not Qualified")

#==================================9.Blocked Account Access==================================
#A user may access an application only if the password is correct and the account is not blocked.
#Store the correct password in a variable.
correct_password = 'Python123!'
#Take the user's password.
password= input("Enter password: ")
#Take blocked status as True or False in the program.
blocked_status = input("is account Blocked (True/False): ")
#Allow access when the password matches and not is_blocked
if password == correct_password and blocked_status == 'False':
    print("Access Granted")
elif password == correct_password and blocked_status == 'True':
    print("Contact Support")
else:
    print("Password is incorrect")


#======================== 10 Library Book Issue Check===============================
#A library issues a book only when the member is active and does not have an overdue book.
#Take member-active status and overdue-book status.
member_active= input("Enter member status (Yes/No): ")
overdue_book_status=input("Enter overdue book status (Yes/No): ")
#Issue the book if member is active and the user does not have an overdue book.
if member_active == 'Yes' and not overdue_book_status == 'Yes':
    print("Book Issued")
#If membership is inactive, print Renew membership first.
elif member_active == 'No':
    print("Renew membership first.")

#If membership is active but overdue exists, print Return overdue book first.
elif member_active == 'Yes' and overdue_book_status =='Yes':
    print("Return overdue book")


#============11. Movie Ticket Age Rule=================================
#A cinema allows entry to an age-restricted movie under two possible paths.
#Take age, whether the person has valid ID, and whether a guardian is present.
age=int(input("Enter age: "))
valid_ID= input("Enter if Person has Valid ID(Yes/No): ")
guardian= input("Enter Guardian(Yes/No): ")
#Allow normal entry when age is at least 18 and valid ID is available.
#Also allow a 16-17 year old when a guardian is present.
#Use parentheses to combine the two valid paths clearly.

if (age >=18 and valid_ID == 'Yes') or (age >=16 and age <18 and guardian =='Yes'):
    print("Entry is Allowed")
else:
    print("You are not Eligible for this Movie")


#===================================12.Employee Work-from-Home Eligibility=========================
# A company allows work from home based on role, performance and security restrictions.
# Take employee role, performance rating and whether the employee is under a security restriction
employee_role=input("Enter Employee Role(Developer/Analyst/PM/Trader):")
performance_rating= int(input("Enter Performance Rating:"))
security_restriction= input("Enter Security Restriction(Yes/No):")

# Allow WFH when role is developer or analyst, performance rating is at least 3, and the employee is not restricted.
if (employee_role == 'Developer' or employee_role == 'Analyst') and performance_rating >= '3' and not security_restriction == 'Yes':
    print("Employee is allowed to Work from Home")

# If role and performance qualify but restriction is active, print WFH blocked by security restriction.
elif (employee_role == 'Developer' or employee_role == 'Analyst') and performance_rating >= '3' and  security_restriction == 'Yes':
    print("WFH is blocked due to security restriction")
# Otherwise print WFH not eligible.
else:
    print("Employee is Not eligible to Work from Home")
# Use parentheses around the role alternatives.


#===============================13.Hospital Appointment Priority============================
#A clinic assigns priority based on age, temperature and emergency status.
#Take patient age, temperature and emergency status.
#Ensure the high-priority rule is checked before the lower-priority rule.
patient_age=int(input("Enter Patient age:"))
temperature= float(input("Enter temperature:"))
emergency_status=input("Enter Emergency status(Yes/No):")
#Assign High Priority if emergency is yes or temperature is 103 or above.
if emergency_status == 'Yes' or temperature >= 103:
    priority="High Priority"
#Assign Priority if age is 65 or above and temperature is at least 100.
elif patient_age>= 65 and temperature >=100:
    priority=" Priority"
else:
    #Otherwise assign Normal Queue.
    priority="Normal Queue"
# Print all patient details and the assigned category.
print("Patient Age:", patient_age)
print("Patient Temperature:", temperature)
print("Patient Priority:", priority)

#=================================14.Scholarship Decision System===============================
#A scholarship program evaluates academic performance, family income and sports achievement
#Take three subject marks and calculate percentage
math_marks=int(input("Enter math marks:"))
science_marks=int(input("Enter science marks:"))
english_marks=int(input("Enter english marks:"))
total_marks=math_marks+science_marks+english_marks
percentage_marks=total_marks/3
#Take annual family income and sports-achievement status.
family_income=int(input("Enter family income:"))
sports_ach_status=input("Enter sports achievement status (Yes/No):")
#Give Full Scholarship if percentage is at least 90 and family income is at most 500,000.
if family_income <= 500000 and percentage_marks>=90:
    scholarship_status='Full Scholarship'
    #Give Merit Scholarship if percentage is at least 85 or sports achievement is yes.
elif percentage_marks>=85 or sports_ach_status == 'Yes':
    scholarship_status='Merit Scholarship'
#Otherwise print Not eligible for scholarship
else:
    scholarship_status='Not eligible for scholarship'
#Print percentage rounded to 2 decimal places along with the final decision.
print("Percentage of the Marks:",round(percentage_marks,2))
print("Your Scholarship Status:",scholarship_status)


#=============================15.Airport Boarding Eligibility System=============================
#Build a simplified airport boarding checker that combines identity, ticket, baggage and special-assistance rules.
#Take passenger name, age, ticket status, valid-ID status, baggage weight and special-assistance status.
passenger_name= input("Enter Passenger Name:")
age= int(input("Enter age:"))
ticket_status=input("Enter ticket status (Valid/NotValid):")
valid_ID= input("Enter Valid ID(Yes/No):")
baggage_weight= float(input("Enter baggage Weight:"))
special_assistance_status=input("Enter special assistance status (Yes/No):")
guardian_status = input("Is a Guardian Present? (Yes/No): ")
#If ticket is not valid, deny boarding regardless of other values.
if not ticket_status == 'Valid':
    message ="Deny Boarding due to InValid Ticket"
#A passenger below 18 may board when ticket is valid and a guardian is present.
elif age <18 and ticket_status == 'Valid' and guardian_status == 'Yes' and valid_ID == 'Yes':
    message= "passenger may board with Guardian"

#A normal adult passenger may board only when ticket is valid and ID is valid and baggage is at most 20 kg.
elif age >=18 and ticket_status == 'Valid' and valid_ID == 'Yes' and baggage_weight <=20:
    message="passenger may board"

#If baggage exceeds 20 kg but all other normal-adult requirements pass, print Pay excess baggage fee before boarding.
elif baggage_weight >20 and ticket_status == 'Valid' and valid_ID == 'Yes':
   message ="Please Pay excess baggage fee before boarding"

    #If special assistance is requested and boarding is otherwise allowed, print an additional assistance message.
if special_assistance_status == 'Yes' and ('may board' in message  or 'may board with Guardian' in message):
    print("Special Assistance is on the way for Boarding")
    #Print a final boarding summary containing passenger name, baggage weight and decision.

print("Passenger Name:",passenger_name)
print("Baggage Weight:",baggage_weight)
print("Final Decision Message  :",message)




