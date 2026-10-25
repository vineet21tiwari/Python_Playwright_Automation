#   ==========10 Largest of Two Numbers > == IF-ELIF-ELSE============
firstno= int(input(print('enter first number :')))
secondno= int(input(print('enter second number :')))
thirdno= int(input(print('enter third number :')))
if firstno>secondno and firstno>thirdno:
  print('biggest number is :',firstno)
elif secondno>firstno and secondno>thirdno:
  print('biggest number is :',secondno)
else: print('biggest number is :',thirdno)

