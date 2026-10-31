# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter another number: "))
#
# print("The sum of two number is: " , number1 + number2)
# print("The product of two number is: ", number1 * number2)
# print("The difference of two number is: ", number1 - number2)
# print("The quotient of two number is: ", round(number1 / number2,2))
# print("the floor division of two number is: ", number1 // number2)
# print("The remainder of two number is: ", number1 % number2)

# applicant_age = int(input("Enter applicant age: "))
# Monthly_salary = float(input("Enter monthly salary: "))
# Credit_score = int(input("Enter credit score: "))
# if applicant_age >= 21 and Monthly_salary >= 30000 and Credit_score >= 700:
#     print("Preliminary check approved.")
# else:
#     print("Not eligible for preliminary check.")
#
#     if applicant_age < 21:
#         print("Reason : Age must be atleast 21")
#
#     if Monthly_salary < 30000:
#         print("Reason : Salary must be atleast 30000")
#
# #     if Credit_score < 700:
#         print("Reason : Credit score must be atleast 700")

correct_username = "python"
correct_password = "PythonPlayWright"

username = input("Enter your username: ")
password = input("Enter your password: ")

is_blocked = False

if username.lower() == correct_username.lower() and correct_password == password:
    print("Access granted")
