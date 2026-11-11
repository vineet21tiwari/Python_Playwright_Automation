available_courses = ["python", "java", "sql", "playwright"]
course_name = input("Enter the course name: ")
course_fee = float(input("Enter the course fee: "))
amount_paid = float(input("Enter the amount already paid: "))

if course_name in available_courses:
    if amount_paid >= 0.5 * course_fee:
        print("Registration successful.")
    else:
        remaining_amount = 0.5 * course_fee - amount_paid
        print(f"Insufficient payment. You need to pay ${remaining_amount:.2f} more to reach 50%.")
else:
    print("Course not available.")
#5.2
valid_coupons = ["SAVE10", "SAVE20", "NEWUSER"]
price = float(input("Enter the item price: "))
quantity = int(input("Enter the item quantity: "))
coupon_code = input("Enter the coupon code: ")
membership_type = input("Enter the membership type (regular/premium): ")

subtotal = price * quantity
if subtotal >= 5000 and coupon_code in valid_coupons:
    discount = subtotal * 0.20
elif subtotal >= 3000 or membership_type == "premium":
    discount = subtotal * 0.10
else:
    discount = 0

final_bill = subtotal - discount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount amount: ${discount:.2f}")
print(f"Final bill: ${final_bill:.2f}")
#5.3
subjects = ["maths", "science", "english", "computer"]
subject = input("Enter subject: ")
if subject in subjects:
    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark {i + 1}: "))
        marks.append(mark)
    attendance = float(input("Enter attendance percentage: "))

    average = sum(marks) / len(marks)

    if average >= 40 and attendance >= 75:
        print("Student is eligible for the final assessment.")
    else:
        if average < 40:
            needed_marks = (40 * len(marks)) - sum(marks)
            print(f"Average is below 40. Student needs {needed_marks:.2f} more marks to reach an average of 40.")
        if attendance < 75:
            shortage = 75 - attendance
            print(f"Attendance is below 75%. Student needs {shortage:.2f}% more attendance to meet the requirement.")
        #5.4
        destinations = ["goa", "delhi", "jaipur", "mumbai"]
        destination = input("Enter destination: ")
        travellers = int(input("Enter number of travellers: "))
        ticket_price = float(input("Enter ticket price per person: "))
        wallet_balance = float(input("Enter wallet balance: "))
        total_cost = travellers * ticket_price

        if destination in destinations:
            if wallet_balance >= total_cost:
                print("Booking successful.")
            else:
                shortage = total_cost - wallet_balance
                print(f"Insufficient balance. You need ${shortage:.2f} more to complete the booking.")
        else:
            print("Destination unavailable.")
    #5.5
    restricted_items = ["chemical", "battery", "aerosol"]
    product_name = input("Enter product name: ").lower()
    total_quantity = int(input("Enter total quantity: "))
    box_capacity = int(input("Enter box capacity: "))

    if product_name in restricted_items:
        print("Shipment blocked.")
    elif total_quantity <= 0 or box_capacity <= 0:
        print("Invalid input.")
    else:
        complete_boxes = total_quantity // box_capacity
        leftover_items = total_quantity % box_capacity
        print(f"Complete boxes: {complete_boxes}")
        print(f"Leftover items: {leftover_items}")

    #5.6
    eligible_departments = ["qa", "engineering", "devops"]
    department = input("Enter your department: ").lower()
    monthly_salary = float(input("Enter your monthly salary: "))
    performance = float(input("Enter your performance score: "))
    experience = int(input("Enter your years of experience: "))
    annual_salary = monthly_salary * 12
    bonus = 0

    if department in eligible_departments:
        if performance >= 80 and experience >= 2:
            bonus = annual_salary * 0.10
        elif performance >= 70 or experience >= 5:
            bonus = annual_salary * 0.05

    final_compensation = annual_salary + bonus
    print(f"Annual Salary: ${annual_salary:.2f}")
    print(f"Bonus Amount: ${bonus:.2f}")
    print(f"Final Annual Compensation: ${final_compensation:.2f}")

#5.7

allowed_roles = ["admin", "manager", "tester"]
blocked_users = ["guest", "demo", "temp"]
username = input("Enter username: ").lower()
role = input("Enter role: ").lower()
balance = float(input("Enter account balance: "))
if role in allowed_roles and username not in blocked_users and balance >= 0:
    print("Access granted.")
if username in blocked_users:
    print("Blocked account.")
elif role not in allowed_roles:
    print("Unauthorized role.")
elif balance < 0:
    print("Insufficient funds.")
else:
    print("Access granted.")

#5.8
    categories = ["comedy", "drama", "action", "horror"]
    category = input("Enter movie category: ").lower()
    age = int(input("Enter your age: "))
    ticket_price = float(input("Enter ticket price: "))
    number_of_tickets = int(input("Enter number of tickets: "))
    wallet_balance = float(input("Enter wallet balance: "))
    total_price = ticket_price * number_of_tickets
    if category in categories and wallet_balance >= total_price:
        if category == "horror" and age >= 18:
            print("Booking confirmed.")
        elif category != "horror" and age >= 13:
            print("Booking confirmed.")
        else:
            print("Booking failed: Age restriction not met.")
    else:
        if category not in categories:
            print("Booking failed: Invalid category.")
        elif wallet_balance < total_price:
            print("Booking failed: Insufficient funds.")


#5.9
service_zones = ["madhapur", "gachibowli", "kondapur", "hitech city"]
delivery_area = input("Enter delivery area: ").lower()
food_total = float(input("Enter food total amount: "))
delivery_charge = float(input("Enter delivery charge: "))
premium_member = input("Are you a premium member? (yes/no): ").lower()

if delivery_area in service_zones and food_total > 0:
    if food_total >= 1000 or premium_member == "yes":
        print("Serviceable.")
        print("Free delivery applied.")
        final_amount = food_total
    else:
        print("Serviceable.")
        print(f"Delivery charge applied: ${delivery_charge:.2f}")
        final_amount = food_total + delivery_charge
else:
    print("Not serviceable.")

print(f"Final payable amount: ${final_amount:.2f}")
#5.10
enrolled_courses = ["python", "playwright", "pytest"]
blocked_users = ["guest", "suspended"]
username = input("Enter your username: ")
selected_course = input("Enter the course you want to access: ")
attendance = float(input("Enter your attendance percentage: "))
lab_credits = int(input("Enter your available lab credits: "))
sessions = int(input("Enter the number of sessions you want to book: "))
required_credits = sessions * 2
remaining_credits = lab_credits - required_credits
if selected_course in enrolled_courses and username not in blocked_users and attendance >= 75 and lab_credits >= required_credits:
    print(f"Access granted. Remaining credits: {remaining_credits}")
else:
    if selected_course not in enrolled_courses:
        print("Access denied. Course not enrolled.")
    if username in blocked_users:
        print("Access denied. User is blocked.")
    if attendance < 75:
        print("Access denied. Attendance is below 75%.")
    if lab_credits < required_creditss:
        print(f"Access denied. Insufficient credits. You need {required_credits - lab_credits} more credits.")


