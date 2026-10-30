# number = int(input("Enter a number: "))
#
# if number > 0:
#     print("I am inside first if block")
#     print("Number is positive")
#
# elif number < 0:
#     print("I am inside second if block")
#     print("Number is negative")
#
# else:
#     print("I am inside else block")
#     print("Number is zero")

##########################################################
# Q7

maths = int(input("Enter maths marks "))
science = int(input("Enter science marks "))
english = int(input("Enter english marks "))

total = maths + science + english
average = total / 3

if average >= 40:
    print("PASS")
    print("Total marks is: ", total, " and average is: ", round(average,2))
else:
    print("FAIL")
    print("Total marks is: ", total, " and average is: ", average)

















