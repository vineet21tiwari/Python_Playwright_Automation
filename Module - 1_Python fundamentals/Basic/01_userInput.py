# age = "15"
# age = int(age)
# print(age +5)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# # print("Your name is ", name)
# # print("Your age is ", age)
# print("Welcome to the course ", name, "your age is ", age)

# input method will always take value as a string only
# firstNumber = int(input("Enter first number: "))
# secondNumber = int(input("Enter second number: "))
#
# print(firstNumber + secondNumber)
# print(firstNumber - secondNumber)
# print(firstNumber * secondNumber)
# divisonResult = firstNumber / secondNumber
# print(round(divisonResult,2))
# print(firstNumber // secondNumber)
# // ---------> is called floor division

#take 3 subject marks from the user (mathsMarks, scienceMarks, EnglishMarks ---------> print average and percentage)
mathsMarks = int(input("Enter maths marks: "))
scienceMarks = int(input("Enter science marks: "))
englishMarks = int(input("Enter english marks: "))

totalMarks = mathsMarks + scienceMarks + englishMarks
averageMarks = totalMarks/3
averageMarks = round(averageMarks,2)

percentage = (totalMarks*100)/300
percentage = round(percentage,2)

print("Average Marks: " + str(averageMarks))
print("Percentage: " + str(percentage) + "%")

