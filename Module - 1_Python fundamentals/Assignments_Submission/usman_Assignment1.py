#   ==========10 Largest of Two Numbers > == IF-ELIF-ELSE============
firstno= int(input(print('enter first number :')))
secondno= int(input(print('enter second number :')))
thirdno= int(input(print('enter third number :')))
if firstno>secondno and firstno>thirdno:
  print('biggest number is :',firstno)
elif secondno>firstno and secondno>thirdno:
  print('biggest number is :',secondno)
else: print('biggest number is :',thirdno)


username='usmanji'
userpin=7151
Employee_loginid = input("Enter employee Userid: ")
Employee_pin = int(input("Enter employee PIN: "))
Employee_isactive = input("Enter if employee is active: ")
if Employee_loginid == username and  Employee_pin == userpin:
    print("Employee login is successful")
else:
    print("Employee login is not successful")
if Employee_isactive != true:
    print("Employee account is not Active")

Visitors_age = int(input("Enter Visitors age: "))
Visitors_Hight = float(input("Enter Visitors Hight: "))
Credit_score = int(input("Enter credit score: "))
if (Visitors_age >= 12
        and Visitors_Hight >= 140):
    print("Preliminary check approved")
elif (Visitors_age < 12 and Visitors_Hight >= 140):
    print("Age requirement not Met")
elif (Visitors_age > 12 and Visitors_Hight < 140):
    print("Hight requirement not Met")
else: print("Ride# allowed only for the fully valid case Visitors")
