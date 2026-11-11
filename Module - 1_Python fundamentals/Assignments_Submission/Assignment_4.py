#4.1
Maths_marks = float(input("Enter Maths marks: "))
Science_marks = float(input("Enter Science marks: "))
English_marks = float(input("Enter English marks: "))
total_marks = Maths_marks + Science_marks + English_marks
average_marks = total_marks / 3
attendance = float(input("Enter attendance percentage: "))

if average_marks >= 40 and attendance >= 75:
    print("PASS - Eligible")
elif average_marks >= 40 and attendance < 75:
    print("Academically passed, attendance shortage")
else:
    print("Not Eligible")

print(f"Total marks: {total_marks}")
print(f"Rounded average: {round(average_marks)}")
print(f"Attendance: {attendance}%")

if average_marks >= 40 and attendance < 75:
    print("Academically passed, attendance shortage")

#4.2
    # <!-- A bank performs a simple preliminary eligibility check before processing a loan application.
    # 1.
    # 2.
    # 3.
    # 4.
    # 5.
    # Take applicant age, monthly salary and credit score.
    # Approve the preliminary check only if age is at least 21, salary is at least 30,000 and credit score is at least 700.
    # If age and salary qualify but credit score is below 700, print Credit score needs improvement.
    # Otherwise print Not eligible for preliminary check.
    # Print all three entered values in the final summary. -->
    applicant_age = int(input("Enter applicant age: "))
    Monthly_salary = float(input("Enter monthly salary: "))
    Credit_score = int(input("Enter credit score: "))
    if applicant_age >= 21 and Monthly_salary >= 30000 and Credit_score >= 700:
        print("Preliminary check approved.")
    elif applicant_age >= 21 and Monthly_salary >= 30000 and Credit_score < 700:
        print("Credit score needs improvement.")
    else:
        print("Not eligible for preliminary check.")
        failure_reason = []
        if applicant_age < 21:
            failure_reason.append("Age is below 21.")
        elif applicant_age < 21 and Monthly_salary < 30000:
            failure_reason.append("Age is below 21 and salary is below 30,000.")
        else:
            failure_reason.append("Salary is below 30,000.")
        print("Failure reason: ", " ".join(failure_reason))

#4.3
# An employee can enter a secure dashboard only when both username and PIN are correct.
# 1.

# 6.
# Store a correct username and correct PIN in variables.
# Take username and PIN from the user.
# If both match, print Login successful.
# Otherwise print Invalid credentials.
# Add a second condition requiring
# account_active == True .
# If credentials are correct but the account is inactive, print a separate message using

username = "admin"
pin = "1234"
print=input("Enter username: ")
pin_input = input("Enter PIN: ")
if print == username and pin_input == pin:
    print("Login successful.")
else:
    print("Invalid credentials.")

    account_active = True
    if print == username and pin_input == pin and account_active:
        print("Login successful.")
    elif print == username and pin_input == pin and not account_active:
        print("Account is inactive. Please contact support.")

#4.4
# A ride is allowed only when the visitor meets both age and height requirements.
# 1.
# 2.
# 3.
# 4.
# 5.
# Take visitor age and height in centimetres.
# Allow the ride only when age is at least 12 and height is at least 140 cm.
# If age qualifies but height does not, print Height requirement not met.
# If height qualifies but age does not, print Age requirement not met.
# Otherwise print Ride allowed only for the fully valid case
visitor_age = int(input("Enter visitor age: "))
visitor_height = float(input("Enter visitor height in cm: "))
if visitor_age >= 12 and visitor_height >= 140:
    print("Ride allowed.")
elif visitor_age >= 12 and visitor_height < 140:
    print("Height requirement not met.")
elif visitor_age < 12 and visitor_height >= 140:
    print("Age requirement not met.")
else:
    print("Both requirements not met.")

#4.5
    # A shopper receives a 10% discount if the order is large enough or if they are a premium member.
    # 1.
    # 2.
    # 3.
    # 4.
    # 5.
    # 6.
    # Take order amount.
    # Take premium-member status as
    # yes or
    # no .
    # If order amount is at least 5000 or the customer is premium, apply a 10% discount.
    # #Otherwise keep the original bill.
    # Print original bill, discount amount and final bill.
    # Add an
    # elif : if order amount is at least 10,000 and the member is premium, give 15% instead.
    order_amount = float(input("Enter order amount: "))
    premium_member = input("Are you a premium member? (yes/no): ")
    if order_amount <= 5000 and premium_member == "yes":
        discount = order_amount * 0.10
    elif order_amount >= 10000 and premium_member == "yes":
        discount = order_amount * 0.15
    else:
        discount = 0

    final_bill = order_amount - discount
    print(f"Original bill: ${order_amount:.2f}")
    print(f"Discount amount: ${discount:.2f}")
    print(f"Final bill: ${final_bill:.2f}")

#4.6
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
# Print the exact reason for the granted access in a separate message.
AccessCard = input("Do you have a valid access card? (yes/no): ").strip().lower()
Role = input("What is your role? (employee/doctor/firefighter/visitor): ").strip().lower()

if AccessCard == "yes" or Role in ["doctor", "firefighter"]:
    print("Entry granted.")
    if AccessCard == "yes":
        print("Reason: Valid access card.")
    else:
        print("Reason: Emergency staff member.")
else:
    print("Entry denied.")

#4.7
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
    # Print cart value, delivery fee and final payable amount.
    cart_value = float(input("Enter the cart value: "))
    membership_status = input("Are you a premium member? (yes/no): ").strip().lower()
    if cart_value >= 999 or membership_status == "yes":
        delivery_fee = 0
    elif 499 <= cart_value < 999 and membership_status == "no":
        delivery_fee = 40
    else:
        delivery_fee = 80
    print("Cart value: ", cart_value)
    print("Delivery fee: ", delivery_fee)
    final_amount = cart_value + delivery_fee
    print("Final payable amount: ", final_amount)
#4.8
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
# Otherwise print selected/not selected appropriately.
race_time = float(input("Enter 100-metre race time (in seconds): "))
endurance_score = int(input("Enter endurance score: "))
attendance_percentage = float(input("Enter attendance percentage: "))
attendance = attendance_percentage >= 75
if (race_time <= 14 or endurance_score >= 80) and attendance_percentage >= 75:
    print("Selected")
elif (race_time <= 14 or endurance_score >= 80) and attendance_percentage < 75:
    print("Performance qualified - attendance insufficient")
else:
    print("Not Selected")

#4.9
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
# Otherwise print Incorrect password.
x = "password123"
user_password = input("Enter your password: ")
is_blocked = bool(input("Is your account blocked? (True/False): "))
print("-------Access Summary-------")
if user_password == x and not is_blocked:
    print("Access granted.")
elif user_password == x and is_blocked:
    print("Contact support.")
else:
    print("Incorrect password.")
#4.10
# A library issues a book only when the member is active and does not have an overdue book.
# Take member-active status and overdue-book status.
# Issue the book if member is active and the user does not have an overdue book.
# If membership is inactive, print Renew membership first.
# If membership is active but overdue exists, print Return overdue book first.
# Use
# not explicitly in at least one condition.
member_active = input("Is the member active? (yes/no): ").strip().lower() == "yes"
overdue_book = input("Does the member have an overdue book? (yes/no): ").strip().lower() == "yes"

if member_active and not overdue_book:
    print("Book issued successfully.")
elif not member_active:
    print("Renew membership first.")
else:
    print("Return overdue book first.")

#4.11
age = int(input("Enter your age: "))
has_valid_id = input("Do you have a valid ID? (yes/no): ").strip().lower()
guardian_present = input("Is a guardian present? (yes/no): ").strip().lower()
allow_entry = (age >= 18 and has_valid_id == "yes") or (16 <= age <= 17 and guardian_present == "yes")
if allow_entry:
    print("Entry allowed.")
else:
    print("Entry denied.")
    additional_message = "You are too young to watch this movie" if age < 16 else ""
    print(additional_message)

#4.12
employee_role = input("Enter employee role (developer/analyst/manager): ").strip().lower()
performance_rating = int(input("Enter performance rating (1-5): "))
is_restricted = input("Is the employee under security restriction? (yes/no): ").strip().lower() == "yes"

allow_wfh = (employee_role == "developer" or employee_role == "analyst") and performance_rating >= 3 and not is_restricted

if allow_wfh:
    print("WFH allowed.")
elif (employee_role == "developer" or employee_role == "analyst") and performance_rating >= 3 and is_restricted:
    print("WFH blocked by security restriction.")
else:
    print("WFH not eligible")
