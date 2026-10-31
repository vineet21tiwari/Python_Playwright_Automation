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
membership_type=input("Enter membership type: ")
#3. Calculate subtotal = price * quantity.
subtotal = item_price * quantity
#4. If subtotal >= 5000 AND coupon is in valid_coupons, apply 20% discount.
if subtotal >=5000 and coupon_code in valid_coupons:
    discount_amount=20/100
#5. Else if subtotal >= 3000 OR membership is premium, apply 10% discount.
elif subtotal >= 3000 or membership_type == "premium":
    discount_amount=10/100
#6. Otherwise apply no discount. Print subtotal, discount amount and final bill
else:
    discount_amount=0
final_bill = subtotal-discount_amount
print("Your subtotal for Today:",subtotal)
print("Your Discount amount:",discount_amount)
print("Your Final Bill:",final_bill)