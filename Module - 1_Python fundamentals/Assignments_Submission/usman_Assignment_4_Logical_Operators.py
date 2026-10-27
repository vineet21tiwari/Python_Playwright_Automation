

# Student Exam Eligibility
# AND
# IF-ELSE
# AVERAGE
# Questions 01-02
# A school allows a student to pass only when academic performance
# and attendance are both acceptable.
#
# Take marks in Maths, Science and English and calculate the average.
# Take attendance percentage.
# If average is at least 40 and attendance is at least 75, print PASS - Eligible.
# Otherwise print Not Eligible.
# Also print total marks, rounded average and attendance.
# Add an
# elif : if average is at least 40 but attendance is below 75
# , print Academically passed, attendance
# shortage.\

Math_marks = int(input("Enter Math Marks: "))
Science_marks = int(input("Enter Science Marks: "))
English_marks = int(input("Enter English Marks: "))
Attendance_percent = int(input("Enter Attendance Percentage: "))
Average_marks = (Math_marks + Science_marks + English_marks)//3
if Average_marks >= 40 and Attendance_percent >= 75:
    print("Passed and Eligible.")
else: print("Not Eligible.")
if Average_marks >= 40 and Attendance_percent < 75:
    print("Academically Passed but Attendance Shortage so Not Eligible.")
#
# 2 Loan Pre-Eligibility Checker
# AND
# IF-ELIF-ELSE
# A bank performs a simple preliminary eligibility check before processing a loan application.
# 1.
# 2.
# 3.
# 4.
# 5.
# Take applicant age, monthly salary and credit score.
# Approve the preliminary check only if age is at least 21, salary is at least 30,000 and credit score is at least 700.
# If age and salary qualify but credit score is below 700, print Credit score needs improvement.
# Otherwise print Not eligible for preliminary check.
# Print all three entered values in the final summary.
# Assignment 04 - Logical Operators

applicant_age = int(input("Enter applicant age: "))
Monthly_salary = float(input("Enter monthly salary: "))
Credit_score = int(input("Enter credit score: "))
if (applicant_age >= 21
        and Monthly_salary >= 30000 and Credit_score >= 700):
    print("Preliminary check approved.")
elif applicant_age >= 21 and Monthly_salary >= 30000 and Credit_score < 700:
    print("Credit score needs improvement.")
else:
    print("Not eligible for preliminary check.")
    print(applicant_age)
    print(Monthly_salary)
    print(Credit_score)