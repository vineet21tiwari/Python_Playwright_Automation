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