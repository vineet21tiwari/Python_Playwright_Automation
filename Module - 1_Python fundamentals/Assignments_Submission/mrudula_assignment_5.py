#============================1.Smart course Registration============================
#1.. Create available_courses = ["python", "java", "sql", "playwright"].
from functools import total_ordering

available_courses = ["python", "java", "sql", "playwright"]
#2. Take course name, course fee and amount already paid from the user.
course_name= input("Enter course name: ")
course_fee =int(input("Enter course fee : "))
amount_paid=int(input("Enter amount paid : "))
#3. Calculate the remaining fee using course_fee - amount_paid.
remaining_fee= course_fee-amount_paid
#4. Registration is successful only if the course is in available_courses AND amount_paid is atleast 50% of the course fee.
if course_name in available_courses and amount_paid >= course_fee / 2:
    print("Registration is Successful")
#5. If the course is valid but payment is insufficient, print how much more is needed to reach 50%.
elif course_name in available_courses and amount_paid < course_fee / 2:
    print("Please pay remaining balance to Enroll for the Course")

#6. If the course is not available, print Course not available
elif course_name not in available_courses:
    print("Course is Not Available")

#=====================2.Online Shopping Coupon Challenge=====================

#An online store provides discounts based on cart value, membership and valid coupon codes.
#1. Create valid_coupons = ["SAVE10", "SAVE20", "NEW USER"].
valid_coupons = ["SAVE10", "SAVE20", "NEW USER"]
#2. Take item price, quantity, coupon code and membership type from the user.
item_price=float(input("Enter item price: "))
quantity=int(input("Enter quantity: "))
coupon_code=input("Enter coupon code: ")
membership_type=input("Enter membership type: ").lower()
#3. Calculate subtotal = price * quantity.
subtotal = item_price * quantity
#4. If subtotal >= 5000 AND coupon is in valid_coupons, apply 20% discount.
if subtotal >=5000 and coupon_code in valid_coupons:
    discount_amount= (subtotal*20)/100
#5. Else if subtotal >= 3000 OR membership is premium, apply 10% discount.
elif subtotal >= 3000 or membership_type == "premium":
    discount_amount=(subtotal*10)/100
#6. Otherwise apply no discount. Print subtotal, discount amount and final bill
else:
    discount_amount=0
final_bill = subtotal-discount_amount
print("Your subtotal for Today:",subtotal)
print("Your Discount amount:",discount_amount)
print("Your Final Bill:",final_bill)


#==================================3 Exam Eligibility & Subject Validation========================================
#A student can sit for the final assessment only for approved subjects and only when both performance and attendance requirements are met.
#1. Create subjects = ["maths", "science", "english", "computer"].
subjects = ["maths", "science", "english", "computer"]
#2. Take subject, three test marks and attendance percentage.
subject= input("Enter the Subject : ").lower()
total_marks= float(input("Enter the Total Marks : "))
attendance_percentage = int(input("Enter attendance : "))
#3. Calculate average marks.
average_marks=total_marks/3
#4. Student is eligible only if subject is in subjects AND average >= 40 AND attendance >= 75.
if subject in subjects and average_marks>=40 and attendance_percentage>= 75:
    print("Student is Eligible")
#5. If subject is valid but average is below 40, print how many more marks are needed to reach 40 average.
elif subject in subjects and average_marks<40 and attendance_percentage>= 75:
    required_marks=40-average_marks
    print("Student is required to get", round(required_marks,3),"to reach 40 average marks")
#6. If attendance is below 75, also print the attendance shortage.
elif attendance_percentage<75:
    print("Attendance shortage for the Exam")


#4=================4 Travel Booking Budget Checker================================
#A travel portal allows bookings only for supported destinations and when the traveller has enough money.
#1. Create destinations = ["goa", "delhi", "jaipur", "mumbai"].
destinations = ["goa", "delhi", "jaipur", "mumbai"]
#2. Take destination, number of travellers, ticket price per person and wallet balance.
destination = input("Enter the Destination : ").lower()
no_of_travellers= int(input("Enter the number of travellers :"))
ticket_price_per_person = float(input("Enter ticket price: "))
wallet_balance  = float(input("Enter wallet balance : "))
#3. Calculate total_cost = travellers * ticket_price.
total_cost = no_of_travellers * ticket_price_per_person
print("Total Cost for this Trip:",total_cost)
#4. Booking succeeds only if destination is in destinations AND wallet balance >= total_cost.
if destination in destinations and wallet_balance >= total_cost:
    print("Your Booking is Successful")
#5. If destination is valid but balance is low, calculate and print the shortage.
elif destination in destinations and wallet_balance < total_cost:
    amount_required=total_cost-wallet_balance
    print("You have Shortage of",amount_required,"for this Trip")
#6. If destination is not supported, print Destination unavailable.
elif destination not in destinations:
    print("Destination is not available")

#========================5 Warehouse Packing & Restricted Items=============================
#A warehouse packs allowed products into boxes but must reject restricted products.
#1. Create restricted_items = ["chemical", "battery", "aerosol"].
restricted_items = ["chemical", "battery", "aerosol"]
#2. Take product name, total quantity and box capacity.
product_name= input("Enter product name: ")
total_quantity= int(input("Enter total quantity : "))
box_capacity= int(input("Enter box capacity : "))

# 3. Continue only if product is not in restricted_items AND quantity > 0 AND box_capacity > 0.
if product_name not in restricted_items and total_quantity > 0 and box_capacity > 0:
    # 4. Calculate complete boxes using // and leftover items using %.
    completeBoxes = total_quantity // box_capacity
    leftOverItems = total_quantity % box_capacity
#5. Print complete boxes and leftovers.
    print("Completed Boxes:",completeBoxes)
    print("Left Over Items:",leftOverItems)
#6. If product is restricted, print Shipment blocked.
elif product_name in restricted_items:
    print("Your Shipment is Blocked")



#=========================== 6.Employee Bonus & Department Check===================================
#A company awards a special bonus only to employees in selected departments who also satisfy performance rules.
#1. Create eligible_departments = ["qa", "engineering", "devops"].
eligible_departments = ["qa", "engineering", "devops"]#
#2. Take department, monthly salary, performance score and years of experience.
department=input("Enter the department : ").lower()
monthly_salary = float(input("Enter monthly salary : "))
performance_score= int(input("Enter performance : "))
years_of_experience = int(input("Enter years of experience : "))
#3. Calculate annual salary = monthly_salary * 12.
annual_salary = monthly_salary * 12
bonus=0
#4. Give a 10% bonus if department is in eligible_departments AND performance >= 80 AND experience >= 2.
if department in eligible_departments and performance_score >=80 and years_of_experience >=2:
    bonus = annual_salary *10/100
#5. Give a 5% bonus if department is eligible AND (performance >= 70 OR experience >= 5).
elif department in eligible_departments and (performance_score>=70 or years_of_experience>=5):
    bonus = annual_salary *5/100
#6. Print annual salary, bonus amount and final annual compensation
final_annual_compensation = annual_salary +bonus
print("Your annual Salary:",annual_salary)
print("Your Bonus:",bonus)
print("Your Final Annual Salary:",round(final_annual_compensation,3))


#==========================7 Secure Login & Role Access============================================
#An application allows login only for recognized roles and must reject blocked usernames.
#1. Create allowed_roles = ["admin", "manager", "tester"] and blocked_users = ["guest", "demo","temp"].
allowed_roles = ["admin", "manager", "tester"]
blocked_users = ["guest", "demo","temp"]
#2. Take username, role and account balance from the user. Convert username and role to lowercase.
username=input("Enter username : ").lower()
role=input("Enter role : ").lower()
account_balance=   float(input("Enter account balance : "))
#3. Access is allowed only if role is in allowed_roles AND username is not in blocked_users AND balance >= 0.
if role in allowed_roles and username not in blocked_users and account_balance>=0:
    print("Your Access is allowed")
#4. If username is blocked, print Blocked account.
elif username  in blocked_users:
    print("Your Access is Blocked")
#5. If role is invalid, print Unauthorized role.
elif role not in allowed_roles:
    print("Unauthorized role")
#6. Otherwise print the reason the access check failed
else:
    print("You are not in the List")


#=============================8 Cinema Booking & Age Rules==================================
# A cinema sells tickets for available movie categories, but some categories have age restrictions.
#1. Create categories = ["comedy", "drama", "action", "horror"].
categories = ["comedy", "drama", "action", "horror"]
#2. Take category, age, ticket price, number of tickets and wallet balance.
category=input("Enter category : ").lower()
age=int(input("Enter age : "))
ticket_price=float(input("Enter ticket price : "))
number_of_tickets=float(input("Enter number of tickets : "))
wallet_balance=float(input("Enter wallet balance : "))
#3. Calculate total price.
total_price= ticket_price*number_of_tickets
#4. Booking is possible only if category is in categories AND wallet balance >= total price.
#5. For horror, age must also be >= 18. For all other listed categories, age must be >= 13.
if category not in categories:
    print("Invalid Category")
elif age<13:
    print("Sorry you are not eligible for your age")
elif category =='horror' and age <18:
    print("You are not eligible to watch Horror movie for your age")
elif wallet_balance<total_price:
    print("You dont have enough Balance to Purchase tickets for Today",total_price)
else:
    print("Booking Confirmed")
    print("Movie",category,"is purchased")
    print("total price:",total_price)
#====================================9.Delivery Zone & Free Shipping==================================
#1. Create service_zones = ["madhapur", "gachibowli", "kondapur", "hitech city"].
service_zones = ["madhapur", "gachibowli", "kondapur", "hitech city"]
#2. Take delivery area, food total, delivery charge and premium-member status.
delivery_area= input("Enter delivery area : ").lower()
food_total= float(input("Enter food total : "))
delivery_charge= float(input("Enter delivery charge : "))
premium_member = input("Enter premium member(Yes/No) : ").lower()
#3. Order can proceed only if area is in service_zones AND food total > 0.
#4. Free delivery applies if food total >= 1000 OR premium member is yes.
if delivery_area not in service_zones:
    print("Sorry, delivery is not available in your area")
elif delivery_area in service_zones and  premium_member=="yes" or food_total>=1000 :
    delivery_charge=0
#5. Otherwise add the delivery charge to the food total.
elif delivery_area in service_zones and 0 < food_total < 999:
    print("Your Delivery Charge for Today",delivery_charge)
#6. Print serviceability, delivery fee charged and final payable amount.
final_payable_amount = delivery_charge + food_total
print("Your Order is deliver to ",delivery_area)
print("Your Delivery Fee for Today",delivery_charge)
print("Your Final Payable Amount:",final_payable_amount)


#===========================10.Automation Lab Access - Master Challenge=====================================
#A training lab grants access based on course enrollment, account status, attendance and available lab credits.
#1. Create enrolled_courses = ["python", "playwright", "pytest"] and blocked_users = ["guest","suspended"].
enrolled_courses = ["python", "playwright", "pytest"]
blocked_users = ["guest","suspended"]
#2. Take username, selected course, attendance, lab credits and number of sessions requested.
username= input("Enter username : ").lower()
selected_course= input("Enter course : ").lower()
attendance= int(input("Enter attendance : "))
lab_credits= int(input("Enter lab credits : "))
noOfSessionsRequested= int(input("Enter number of sessions requested : "))
#3. Each session costs 2 credits. Calculate required_credits = sessions * 2 and remaining_credits after booking.
required_credits = noOfSessionsRequested * 2

#4. Access is allowed only if course is in enrolled_courses AND username is not in blocked_users AND attendance >= 75 AND lab_credits >= required_credits.
#5. If credits are insufficient, print how many more credits are needed.
#6. If access is allowed, print remaining credits. Otherwise print every applicable reason for rejection.
if selected_course not in enrolled_courses:
    print("Invalid Course selection")
if username in blocked_users:
    print("Invalid Username")
if attendance<75:
    print("Insufficient Attendance")
if lab_credits < required_credits:
    extra_credits_needed=required_credits-lab_credits
    print("You need more",extra_credits_needed,"Credits")
if selected_course in enrolled_courses and username not in blocked_users and attendance >= 75 and lab_credits >= required_credits:
    remaining_credits=lab_credits-required_credits
    print("You are enrolled in course ", selected_course,"with Credits used ", required_credits,"and remaining credits left",remaining_credits)



