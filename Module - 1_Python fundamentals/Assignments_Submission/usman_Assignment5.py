# 1Smart Course Registration
# IN
# AND
# ARITHMETIC
# A training institute accepts registrations only for courses currently offered and only when the payment
# requirements are satisfied.
# 1. Create available_courses = ["python", "java", "sql", "playwright"].
# 2. Take course name, course fee and amount already paid from the user.
# 3. Calculate the remaining fee using course_fee - amount_paid.
# 4. Registration is successful only if the course is in available_courses AND amount_paid is at
# least 50% of the course fee.
# 5. If the course is valid but payment is insufficient, print how much more is needed to reach
# 50%.
# 6. 000If the course is not available, print Course not available
from itertools import product

course_tojoin = input("Enter course to join: ")
course_fee=float(input("Enter course fee: "))
amount_paid = float(input("Enter amount paid: "))
course_available = ['python','playwright','java','sql']
if course_tojoin in course_available and amount_paid>= course_fee//2:
    print("That course trgistration is successful")
else: print("That course is not available")

# 2 Online Shopping Coupon Challenge
# IN
# OR
# * /
# IF-ELIF-ELSE
# An online store provides discounts based on cart value, membership
# and valid coupon codes.
# 1. Create valid_coupons = ["SAVE10", "SAVE20", "NEWUSER"].
# 2. Take item price, quantity, coupon code and membership type from the user.
# 3. Calculate subtotal = price * quantity.
# 4. If subtotal >= 5000 AND coupon is in valid_coupons, apply 20% discount.
# 5. Else if subtotal >= 3000 OR membership is premium, apply 10% discount.
# 6. Otherwise apply no discount. Print subtotal, discount amount and final bill

membership_type = input("Enter users Membership coupon Type: ")
item_price=float(input("Enter Item Price: "))
item_quantity = float(input("Enter Item Quantity: "))
coupon_available = ['SAVE10','SAVE20','NEWUSER']
sub_total = item_price*item_quantity
if sub_total>=5000 and  membership_type in coupon_available:
    final_bill= sub_total-sub_total*.20
elif sub_total>=3000 and membership_type=='premium':
    final_bill= sub_total-sub_total*.10
else: final_bill= sub_total
print(final_bill)

#3  Exam Eligibility & Subject Validation
# IN
# AND
# AVERAGE
# A student can sit for the final assessment only for approved subjects and only when both performance and
# attendance requirements are met.
# 1. Create subjects = ["maths", "science", "english", "computer"].
# 2. Take subject, three test marks and attendance percentage.
# 3. Calculate average marks.
# 4. Student is eligible only if subject is in subjects AND average >= 40 AND attendance >= 75.
# 5. If subject is valid but average is below 40, print how many more marks are needed to reach
# 40 average.
# 6. If attendance is below 75, also print the attendance shortage.

student_subjects=input("Enter student subject: ")
student_marks=int(input("Enter student marks in subject: "))
subjects_available = ['math','english','science','computer']
student_attendence_percent= int(input("Enter student attendance percentage: "))

if student_subjects in subjects_available and student_marks>=40 and student_attendence_percent>=75:
  print("That subject is available and student is passed")
else: print("That subject is not eligible")

#  4 Travel Booking Budget Checker
# IN
# AND
# A travel portal allows bookings only for supported destinations and
# when the traveller has enough money.
# 1. Create destinations = ["goa", "delhi", "jaipur", "mumbai"].
# 2. Take destination, number of travellers, ticket price per person
# and wallet balance.
# 3. Calculate total_cost = travellers * ticket_price.
# 4. Booking succeeds only if destination is in destinations
# AND wallet balance >= total_cost.
# 5. If destination is valid but balance is low,
# calculate and print the shortage.
# 6. If destination is not supported, print Destination unavailable.

Enter_Destination=input("Enter Destination to go: ")
Enter_Ticket_Price=float(input("Enter Destination Ticket Price: "))
wallet_balance=float(input("Enter Wallet Balance: "))
Number_of_Travellers=int(input("Enter Total Number of Travellers: "))
destinations_available = ['goa','delhi','jaipur','mumbai']
Total_Cost = Enter_Ticket_Price*Number_of_Travellers

if Enter_Destination in destinations_available and Total_Cost<=wallet_balance:
    print("That destination is available and booking is successful")
elif Enter_Destination in destinations_available and Total_Cost>wallet_balance:
    shortage = Total_Cost-wallet_balance
else: print("That destination is not supported")

#  5 Warehouse Packing & Restricted Items
# NOT IN
# // %
# AND
# A warehouse packs allowed products into boxes but must
# reject restricted products.
# 1. Create restricted_items = ["chemical", "battery", "aerosol"].
# 2. Take product name, total quantity and box capacity.
# 3. Continue only if product is not in restricted_items AND quantity > 0
# AND box_capacity > 0.
# 4. Calculate complete boxes using // and leftover items using %.
# 5. Print complete boxes and leftovers.
# 6. If product is restricted, print Shipment blocked

product_name= input("Enter product name: ")
total_quantity=int(input("Enter quantity: "))
box_capacity= int(input("Enter box capacity: "))
restricted_items = ["chemical", "battery", "aerosol"]

product_name= input("Enter product name: ")
total_quantity=int(input("Enter quantity: "))
box_capacity= int(input("Enter box capacity: "))
restricted_items = ["chemical", "battery", "aerosol"]

if product_name not in restricted_items and total_quantity >0 and box_capacity>0:
   ioial_complete_boxs = box_capacity//total_quantity
   leftovers = box_capacity%total_quantity
   print(ioial_complete_boxs)
   print(leftovers)
else:
   print("That product is Restricted")

#  6   Employee Bonus & Department Check
# IN
# AND / OR
# %
# A company awards a special bonus only to employees in
# selected departments who also satisfy performance
# rules.
# 1. Create eligible_departments = ["qa", "engineering", "devops"].
# 2. Take department, monthly salary, performance score
# and years of experience.
# 3. Calculate annual salary = monthly_salary * 12.
# 4. Give a 10% bonus if department is in eligible_departments
# AND performance >= 80 AND
# experience >= 2.
# 5. Give a 5% bonus if department is eligible AND (performance >= 70 OR experience >= 5).
# 6. Print annual salary, bonus amount and final annual compensation

eligible_departments = ["qa", "engineering", "devops"]
department = input("Enter department: ")
monthly_salary = int(input("Enter monthly salary: "))
performance_score= int(input("Enter performance score: "))
years_of_experience= int(input("Enter years of experience: "))
annual_salary = monthly_salary*12
if department in eligible_departments and performance_score >= 70 or years_of_experience >= 5:

 bonus =  annual_salary*.05
 print("bonus amount:" bonus)
 print("annual salary is:" annual_salary)
 print(years_of_experience)
 final_annual_salary = annual_salary+bonus
 print(final_annual_salary)

# 7 Secure Login & Role Access
# IN / NOT IN
# AND
# NOT
# An application allows login only for recognized roles
# and must reject blocked usernames.
# 1. Create allowed_roles = ["admin", "manager", "tester"] and blocked_users = ["guest", "demo",
# "temp"].
# 2. Take username, role and account balance from the user.
# Convert username and role to
# lowercase.
# 3. Access is allowed only if role is in allowed_roles
# AND username is not in blocked_users AND
# balance >= 0.
# 4. If username is blocked, print Blocked account.
# 5. If role is invalid, print Unauthorized role.
# 6. Otherwise print the reason the access check failed



username = input("Enter username: ")
role = input("Enter role: ")
allowed_roles = ["admin", "manager", "tester"]
blocked_users = ["guest", "demo","temp"]
account_balance =int(input("Enter account balance: "))

if role in allowed_roles and username not in blocked_users and account_balance>0:
    print("Tha access is allowed for this user:", username)
elif role in allowed_roles and username  in blocked_users:
    print("That user is blocked")
elif role not in allowed_roles and username not in blocked_users:
     print("That user doesn't have allowed role")
else: print("That user account balance ys zero")

# 8 Cinema Booking & Age Rules
# IN
# AND / OR
# *
# A cinema sells tickets for available movie categories,
# but some categories have age restrictions.
# 1. Create categories = ["comedy", "drama", "action", "horror"].
# 2. Take category, age, ticket price, number of tickets and wallet balance.
# 3. Calculate total price.
# 4. Booking is possible only
# if category is in categories AND wallet balance >= total price.
# 5. For horror, age must also be >= 18. For all other listed categories
# , age must be >= 13.
# 6. Print either Booking confirmed or the exact reason it failed


categories = ["comedy", "drama", "action", "horror"]
category = input("Enter category: ")
age = int(input("Enter age: "))
ticket_price= int(input("Enter ticket price: "))
number_of_tickets = int(input("Enter number of tickets: "))
wallet_balance= int(input("Enter wallet balance: "))
total_price= ticket_price*number_of_tickets

print(total_price)
if category in categories and total_price>wallet_balance:
    print("That booking is not possible because of shortage of money")
elif category == 'horror' and age<18:
    print("That booking is not possible as age is less than 18")
elif category != 'horror' and age<13:
    print("That booking is not possible as age is less than 13")
elif category not in categories and total_price<=wallet_balance:
    print("That booking is not possible because of not in valid category")
else: print("That booking is confirmed")

# 9 Delivery Zone & Free Shipping
# IN
# AND / OR
# A food delivery app checks whether an address is serviceable
# and whether the order qualifies for free delivery.
# 1. Create service_zones = ["madhapur", "gachibowli", "kondapur", "hitech city"].
# 2. Take delivery area, food total, delivery charge
# and premium-member status.
# 3. Order can proceed only if area is in service_zones AND food total > 0.
# 4. Free delivery applies if food total >= 1000 OR premium member is yes.
# 5. Otherwise add the delivery charge to the food total.
# 6. Print serviceability, delivery fee charged and final payable amount

delivery_area = input("Enter delivery area: ")
food_total = float(input("Enter food total: "))
delivery_charge = int(input("Enter delivery charge: "))
premium_member_status=input("Enter premium member status: yes or no ")
service_zones = ["madhapur", "gachibowli", "kondapur", "hitech city"]

if premium_member_status == "no" and delivery_area not in service_zones and food_total<0:
    print("That delivery area is not eligible for serviceand member status is not eligible for free delivery and food total is negative")
elif premium_member_status == "no" and delivery_area not in service_zones and food_total>0:
    print("That delivery area is not eligible for service and member status is not eligible for free delivery but food total is greater than zero")
elif premium_member_status == "no" and delivery_area  in service_zones and food_total>0:
    print("That delivery area is  eligible for service but member status is not eligible for free delivery and food total is greater than zero")
    final_price = food_total+delivery_charge
    print("final_price:",final_price)
elif  delivery_area  in service_zones and premium_member_status == "no" or food_total>1000:
    print("That delivery area is  eligible for service and member status is  eligible for free delivery as food total is greater than 1000")
     final_price = food_total-delivery_charge
    print("final_price:",final_price)
else:  print("That delivery area is eligible for service and free delivery")
final_price = food_total - delivery_charge
print("final_price:",final_price)

# 10: Automation Lab Access - Master Challenge
# IN / NOT IN
# AND / OR / NOT
# ARITHMETIC
# A training lab grants access based on
# course enrollment, account status, attendance and available lab credits.
# 1. Create enrolled_courses = ["python", "playwright", "pytest"]
# and blocked_users = ["guest",
# "suspended"].
# 2. Take username, selected course, attendance, lab credits
# and number of sessions requested.
# 3. Each session costs 2 credits.
# Calculate required_credits = sessions * 2 and
# remaining_credits after booking.
# 4. Access is allowed only if course is in enrolled_courses
# AND username is not in blocked_users
# AND attendance >= 75 AND lab_credits >= required_credits.
# 5. If credits are insufficient, print how many more credits are needed.
# 6. If access is allowed, print remaining credits. Otherwise print every applicable reason for
# rejection
# course_enrollment  in enrolled_courses and user_name  not in blocked_users and attendance >= 75 and available_lab_credits >= required_credits:


enrolled_courses = ["python", "playwright", "pytest"]
blocked_users = ["guest","suspended"]
user_name = input("Enter User Name: ")

course_enrollment =input("Enter course enrollment: ")
account_status=input("Enter account status: ")
attendance=int(input("Enter attendance: "))
available_lab_credits=int(input("Enter available lab credits: "))
number_of_sessions_requested=int(input("Enter number of sessions requested: "))
required_credits = number_of_sessions_requested * 2
remaining_credits =available_lab_credits-required_credits
if course_enrollment not in enrolled_courses or user_name in blocked_users or attendance < 75 or available_lab_credits < required_credits:
  print("That user is not allowed for course enrollment due to below reason")
if course_enrollment not in enrolled_courses:
    print("That course enrollment is not eligible for course not in enrollment list")
elif user_name  in blocked_users:
    print("That user  is  a blocked user  for course enrollment")
elif attendance < 75:
    print("That attendance is not eligible for course enrollment")
elif available_lab_credits < required_credits:
    print("That lab credits is not enough for course enrollment")
else:
    print("That oser is  eligible for course enrollment")
