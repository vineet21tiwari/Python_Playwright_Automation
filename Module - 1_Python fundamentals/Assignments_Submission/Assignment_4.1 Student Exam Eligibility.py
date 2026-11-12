# A school allows a student to pass only when academic performance and attendance are both acceptable.
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# 6. 
# Take marks in Maths, Science and English and calculate the average.
# Take attendance percentage.
# If average is at least 40 and attendance is at least 75, print PASS - Eligible.
# Otherwise print Not Eligible.
# Also print total marks, rounded average and attendance.
# Add an 
# elif : if average is at least 40 but attendance is below 75, print Academically passed, attendance
# shortage.
Maths_marks = float(input("Enter Maths marks: "))
Science_marks = float(input("Enter Science marks: "))   
English_marks = float(input("Enter English marks: "))
total_marks = Maths_marks + Science_marks + English_marks
average_marks = total_marks / 3
attendance = float(input("Enter attendance percentage: "))

if average_marks >= 40 and attendance >= 75:
    print("PASS - Eligible")
elif average_marks >= 40 and attendance < 75:
    print("Academically passed, attendance shortage")
else:
    print("Not Eligible")

print(f"Total marks: {total_marks}")
print(f"Rounded average: {round(average_marks)}")
print(f"Attendance: {attendance}%") 

if average_marks >= 40 and attendance < 75:
    print("Academically passed, attendance shortage")   
    