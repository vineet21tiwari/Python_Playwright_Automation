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