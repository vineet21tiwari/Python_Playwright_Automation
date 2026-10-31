#============================1.Smart course Registration============================
#1.. Create available_courses = ["python", "java", "sql", "playwright"].
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
