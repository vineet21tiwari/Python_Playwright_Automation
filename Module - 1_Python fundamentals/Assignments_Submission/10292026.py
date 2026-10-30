# email = input("Enter email")
# if("@" in email) and ("." in email):
#     print ("Email is valid")
# else:
#     print ("Email is Not valid with @ & .")

# courses = ["Python","Playwright","C++","Cypress"]
# if "Cypress" in courses:
#     print('cypress course is Available')
# else:
#     print  ('Your requested Course is Not Available')

subjects= ["Maths","Science","English"]
marks= int(input("Enter Total Marks:"))
attendance= int(input("Enter Attendance Percentage:"))
subject= input("Enter the Subject:")
if marks>=40 and attendance>=75 and subject in subjects:
    print("Student is Eligible")
else:
    print("Student is Not Eligible")