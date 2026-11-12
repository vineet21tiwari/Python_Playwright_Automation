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
    if lab_credits < required_credits:
        print(f"Access denied. Insufficient credits. You need {required_credits - lab_credits} more credits.")
