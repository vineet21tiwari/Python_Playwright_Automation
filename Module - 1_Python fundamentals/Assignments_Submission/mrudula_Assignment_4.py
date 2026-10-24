# ==========1 Student Exam Eligibility AND IF-ELSE AVERAGE ===============
#A school allows a student to pass only when academic performance and attendance are both acceptable.
from Class_10082026 import science_Marks
from Elif import average_marks

#Take marks in Maths, Science and English and calculate the average.
math_marks = int(input("Enter math marks: "))
science_Marks = int(input("Enter science marks: "))
english_Marks = int(input("Enter english marks: "))
#Take attendance percentage.
attendance_percentage = float(input("Enter attendance percentage: "))
total_marks = math_marks + science_Marks + english_Marks
average_marks = total_marks / 3

#If average is at least 40 and attendance is at least 75, print PASS - Eligible.
if average_marks >=40 and attendance_percentage >=75:
    print("Student is PASS-Eligible")

#Add an elif : if average is at least 40 but attendance is below 75, print Academically passed, attendance shortage.
elif average_marks ==40 and attendance_percentage<75:
    print("Student is Academically passed, attendance shortage")
 #   Otherwise print Not Eligible.
else:
    print("Student is FAIL-Eligible")
#Also print total marks, rounded average and attendance.
print("Total Marks:", total_marks)
print("Average Marks:", round(average_marks,3))
print("Student Attendance Percentage:",attendance_percentage)