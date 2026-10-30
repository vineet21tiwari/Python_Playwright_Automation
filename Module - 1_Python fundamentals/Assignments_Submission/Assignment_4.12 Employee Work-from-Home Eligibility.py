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
