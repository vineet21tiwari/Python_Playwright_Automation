# A school allows a student to pass only when academic performance and attendance are both acceptable.
#
# Take marks in Maths, Science and English and calculate the average.
# Take attendance percentage.
# If average is at least 40 and attendance is at least 75, print PASS - Eligible.
# Otherwise print Not Eligible.
# Also print total marks, rounded average and attendance.
# Add an
# elif : if average is at least 40 but attendance is below 75, print Academically passed, attendance
# shortage
#
# Marks_Math = float(input("Enter Marks Math: "))
# Marks_Science = float(input("Enter Marks Science: "))
# Marks_English = float(input("Enter Marks English: "))
# Total_marks = (Marks_Math + Marks_Science + Marks_English )
# average_marks = (Marks_Math + Marks_Science + Marks_English ) / 3
# attendance = float(input("Enter attendance: "))
# print("Average Marks: ", average_marks)
# print("Total_marks: ", Total_marks)
# print(f"Rounded average: {round(average_marks)}")
# print(f"Round attendance: {round(attendance)}")
# if average_marks >= 40 and attendance >= 75:
#    print("print PASS - Eligible")
# elif average_marks <=40 and attendance < 75:
#         print("Academically passed, attendance shortage")
# else:
#     print ("Not Eligible")


# email= input("enter the email")
# if "@" in email and "." in email:
#     print("email is valid")
# else:
#     print("email is not valid")

# courses =["python","c++","Java","SQL","Playwright"]
# course = input("Enter the course : ")
# if course in courses:
#     print("course is avaible")
# else:
#     print("course is not avaible")
#
# Marks = int(input("Enter Marks : "))
# Attendance = int(input("Enter Attendance: "))
# Subject = input("Enter Subject: "))
# allowed_subject = ["maths","science","english"]
# if Subject in allowed_subject and Marks >=40 and attendance >=75:
#     print("student is eligible")
# else:
#     print("student is not eligible")
subjects= ["Maths","Science","English"]
marks= int(input("Enter Total Marks:"))
attendance= int(input("Enter Attendance Percentage:"))
subject= input("Enter the Subject:")
if marks>=40 and attendance>=75 and subject in "subjects":
    print("Student is Eligible")
else:
    print("Student is Not Eligible")