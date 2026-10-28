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
        

    