# PROBLEM 1 - STUDENT ACADEMIC REPORT & SCHOLARSHIP
#   Store the five fixed subject names in a tuple: English, Maths
#   , Physics, Chemistry and Computer. Take
# the student name and roll number as input.
# b.  Take marks for all five subjects and store them in a list.
# Each mark must be between 0 and 100. If an
# invalid mark is entered, keep asking for that subject
# until a valid mark is given using a while loop.
# c.  Calculate total marks, percentage and average.
# Count how many subjects have marks at least 75 and
# how many subjects are failed. A subject is
# failed when marks are below 40.
# d.  Find the highest and lowest marks manually using a loop.
# Also print the corresponding subject name
# using the matching list/tuple index.
# e.  Use if/elif/else to assign a grade:
# A+ for 90+, A for 80-89.99, B for 70-79.99, C for 60-69.99, D for
# 40-59.99, otherwise Fail.
# f.  A scholarship is awarded only when percentage is at
# least 85 and no subject is failed. Print the
# scholarship decision and reason.
# g.  Create a final dictionary named report
# containing at least: name, roll number, percentage, grade,
# highest mark, lowest mark, pass/fail status and scholarship status.
# Print every key-value pair using
# items()

subjects = ("English", "Maths", "Physics", "Chemistry", "Computer")
for i in range(1,5):
    Name=input('please enter the name of the student:')
    roll_number =input(print('please enter Students Roll Number :'))
    English_Marks=int(input('please enter the English Marks aquired:'))
    while English_Marks<0 or English_Marks>100:
        English_Marks = int(input('please enter Valid English Marks aquired:'))
    Maths_Marks=int(input('please enter the Maths Aquired:'))
    while Maths_Marks<0 or Maths_Marks>100 or type(Maths_Marks)!=int:
        Maths_Marks = int(input('please enter Valid Math Marks Aquired:'))
    Physics_Marks=int(input('please enter the Physics Aquired:'))
    while Physics_Marks<0 or Physics_Marks>100 or type(Physics_Marks)!=int:
        Maths_Marks = int(input('please enter valid Physics Marks Aquired:'))
    Chemistry_Marks=int(input('please enter the Chemistry Aquired:'))
    while Chemistry_Marks<0 or Chemistry_Marks>100 or type(Chemistry_Marks)!=int:
        Chemistry_Marks = int(input('please enter Valid Chemistry Marks Aquired:'))
    Computer_Marks=int(input('please enter the Computer Aquired:'))
    while Computer_Marks<0 or Computer_Marks>100 or type(Computer_Marks)!=int:
        Computer_Marks = int(input('please enter Valid Computer Marks Aquired:'))
Total_Marks= English_Marks + Maths_Marks + Physics_Marks + Chemistry_Marks + Computer_Marks
Average_Marks = Total_Marks/len(subjects)
percentage_Marks = float(Total_Marks/500)*100.0
print('Total Marks Aquired is:',Total_Marks)
print("Average Marks is:",Average_Marks)
print("Percentage Marks is:",percentage_Marks)
highest_mark=100
Lowest_Mark=0
for subject in subjects:
    # if English_Marks == highest_mark:
    #     print("English Marks Aquired are Highest Marks is:",highest_mark)
    # elif Maths_Marks == highest_mark:
    #     print("Math  Marks Aquired are Highest Marks is:", highest_mark)
    # elif Physics_Marks == highest_mark:
    #     print("Physics Marks Aquired are Highest Marks is:", highest_mark)
    # elif Chemistry_Marks == highest_mark:
    #     print("Chemistry Marks Aquired are Highest Marks is:", highest_mark)
    # elif Computer_Marks == highest_mark:
    #     print("Computer Marks Aquired are Highest Marks is:", highest_mark)
    if English_Marks > Maths_Marks and English_Marks > Physics_Marks and English_Marks > Chemistry_Marks and English_Marks > Computer_Marks:
        highest_mark=English_Marks
        print("English Marks Aquired are Highest Marks is:", highest_mark)
    elif Maths_Marks>Physics_Marks  and Maths_Marks>Chemistry_Marks and Maths_Marks>Computer_Marks:
        highest_mark=Maths_Marks
        print("Math  Marks Aquired are Highest Marks is:", highest_mark)
    elif Physics_Marks>Chemistry_Marks and Physics_Marks>Computer_Marks:
        highest_mark=Physics_Marks
        print("Physics Marks Aquired are Highest Marks is:", highest_mark)
    elif Chemistry_Marks>Computer_Marks:
        highest_mark=Chemistry_Marks
        print("Chemistry Marks Aquired are Highest Marks is:", highest_mark)
    else:
        highest_mark=Computer_Marks
        print("Computer Marks Aquired are Highest Marks is:", highest_mark)
#  Lowest Marks
#     if English_Marks == Lowest_Mark:
#         print("English Marks Aquired are Lowest Marks is:", Lowest_Mark)
#     elif Maths_Marks == Lowest_Mark:
#         print("Math  Marks Aquired are Lowest Marks is:", Lowest_Mark)
#     elif Physics_Marks == Lowest_Mark:
#         print("Physics Marks Aquired are Lowest Marks is:", Lowest_Mark)
#     elif Chemistry_Marks == Lowest_Mark:
#         print("Chemistry Marks Aquired are Lowest Marks is:", Lowest_Mark)
#     elif Computer_Marks == Lowest_Mark:
#         print("Computer Marks Aquired are Lowest Marks is:", Lowest_Mark)
    if English_Marks < Maths_Marks and English_Marks < Physics_Marks and English_Marks < Chemistry_Marks and English_Marks < Computer_Marks:
        Lowest_Mark = English_Marks
        print("English Marks Aquired are Lowest Marks is:", Lowest_Mark)

    elif Maths_Marks < Physics_Marks and Maths_Marks<Chemistry_Marks and Maths_Marks < Computer_Marks:
        Lowest_Mark = Maths_Marks
        print("Math  Marks Aquired are Lowest Marks is:", Lowest_Mark)
    elif Physics_Marks < Chemistry_Marks and Physics_Marks < Computer_Marks:
        Lowest_Mark = Physics_Marks
        print("Physics Marks Aquired are Lowest Marks is:", Lowest_Mark)
    elif Chemistry_Marks < Computer_Marks:
        Lowest_Mark = Chemistry_Marks
        print("Chemistry Marks Aquired are Lowest Marks is:", Lowest_Mark)
    else:
        Lowest_Mark = Computer_Marks
        print("Computer Marks Aquired are Lowest Marks is:", Lowest_Mark)
    if English_Marks >= 90:
        print('The Grade aquired in English is A+')
    elif English_Marks < 90 and English_Marks >= 80:
        print('The Grade aquired in English is A')
    elif English_Marks < 80 and English_Marks >= 70:
        print('The Grade aquired in English is B+')
    elif English_Marks < 70 and English_Marks >= 60:
        print('The Grade aquired in English is B')
    elif English_Marks < 60 and English_Marks >= 50:
        print('The Grade aquired in English is C')
    elif English_Marks < 50 and English_Marks >= 45:
        print('The Grade aquired in English is D')
    else:
        print('The Grade aquired in English is FAIL')
    if Maths_Marks >= 90:
        print('The Grade aquired in Math is A+')
    elif Maths_Marks < 90 and Maths_Marks >= 80:
        print('The Grade aquired in Math is A')
    elif Maths_Marks < 80 and Maths_Marks >= 70:
        print('The Grade aquired in Math is B+')
    elif Maths_Marks < 70 and Maths_Marks >= 60:
        print('The Grade aquired in Math is B')
    elif Maths_Marks < 60 and Maths_Marks >= 50:
        print('The Grade aquired in Math is C')
    elif Maths_Marks < 50 and Maths_Marks >= 45:
        print('The Grade aquired in Math is D')
    else:
        print('The Grade aquired in Math is FAIL')
    if Physics_Marks >= 90:
        print('The Grade aquired in Phycics is A+')
    elif Physics_Marks < 90 and Physics_Marks >= 80:
        print('The Grade aquired in Phycics is A')
    elif Physics_Marks < 80 and Physics_Marks >= 70:
        print('The Grade aquired in Phycics is B+')
    elif Physics_Marks < 70 and Physics_Marks >= 60:
        print('The Grade aquired in Phycics is B')
    elif Physics_Marks < 60 and Physics_Marks >= 50:
        print('The Grade aquired in Phycics is C')
    elif Physics_Marks < 50 and Physics_Marks >= 45:
        print('The Grade aquired in Phycics is D')
    else:
        print('The Grade aquired in Phycics is FAIL')
    if Chemistry_Marks >= 90:
        print('The Grade aquired in Chemistry is A+')
    elif Chemistry_Marks < 90 and Chemistry_Marks >= 80:
        print('The Grade aquired in Chemistry is A')
    elif Chemistry_Marks < 80 and Chemistry_Marks >= 70:
        print('The Grade aquired in Chemistry is B+')
    elif Chemistry_Marks < 70 and Chemistry_Marks >= 60:
        print('The Grade aquired in Chemistry is B')
    elif Chemistry_Marks < 60 and Chemistry_Marks >= 50:
        print('The Grade aquired in Chemistry is C')
    elif Chemistry_Marks < 50 and Chemistry_Marks >= 45:
        print('The Grade aquired in Chemistry is D')
    else:
        print('The Grade aquired in Chemistry is FAIL')
    if Computer_Marks >= 90:
        print('The Grade aquired in Computers is A+')
    elif Computer_Marks < 90 and Computer_Marks >= 80:
        print('The Grade aquired in Computers is A')
    elif Computer_Marks < 80 and Computer_Marks >= 70:
        print('The Grade aquired in Computers is B+')
    elif Computer_Marks < 70 and Computer_Marks >= 60:
        print('The Grade aquired in Computers is B')
    elif Computer_Marks < 60 and Computer_Marks >= 50:
        print('The Grade aquired in Computers is C')
    elif Computer_Marks < 50 and Computer_Marks >= 45:
        print('The Grade aquired in Computers is D')
    else:
        print('The Grade aquired in Computers is FAIL')
    if percentage_Marks >= 85 and English_Marks >= 45 and Maths_Marks >= 45 and Physics_Marks >= 45 and Chemistry_Marks >= 45 and Computer_Marks >= 45:
        print('The Student is Qualified for Scholarship:')
    else:
        print('The Student is Not Qualified for Scholarship:')
        if English_Marks < 45:
          print('The Student is Not Qualified for Scholarship coz student FAILD in English:')
        elif Maths_Marks < 45:
          print('The Student is Not Qualified for Scholarship coz student FAILD in Math:')
        elif Physics_Marks < 45:
          print('The Student is Not Qualified for Scholarship coz student FAILD in Physics:')
        elif Chemistry_Marks < 45:
          print('The Student is Not Qualified for Scholarship coz student FAILD in Chemistry:')
        else:
            print('The Student is Not Qualified for Scholarship coz student FAILD in Computer:')



