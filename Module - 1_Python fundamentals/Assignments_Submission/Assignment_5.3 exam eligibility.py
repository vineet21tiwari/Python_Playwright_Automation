subjects = ["maths", "science", "english", "computer"]
subject = input("Enter subject: ")
if subject in subjects:
    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark {i + 1}: "))
        marks.append(mark)
    attendance = float(input("Enter attendance percentage: "))

    average = sum(marks) / len(marks)

    if average >= 40 and attendance >= 75:
        print("Student is eligible for the final assessment.")
    else:
        if average < 40:
            needed_marks = (40 * len(marks)) - sum(marks)
            print(f"Average is below 40. Student needs {needed_marks:.2f} more marks to reach an average of 40.")
        if attendance < 75:
            shortage = 75 - attendance
            print(f"Attendance is below 75%. Student needs {shortage:.2f}% more attendance to meet the requirement.")