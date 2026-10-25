 # ==========1 Student Exam Eligibility AND IF-ELSE AVERAGE ===============
#A school allows a student to pass only when academic performance and attendance are both acceptable.
#Take marks in Maths, Science and English and calculate the average.
math_marks = int(input("Enter math marks: "))
science_Marks = int(input("Enter science marks: "))
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




