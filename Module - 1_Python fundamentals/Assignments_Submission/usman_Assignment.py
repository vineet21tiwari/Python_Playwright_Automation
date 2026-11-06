#Assignment 1:##################################################
firstno= int(input(print('enter first number :')))
secondno= int(input(print('enter second number :')))
thirdno= int(input(print('enter third number :')))
if firstno>secondno and firstno>thirdno:
  print('biggest number is :',firstno)
elif secondno>firstno and secondno>thirdno:
  print('biggest number is :',secondno)
else: print('biggest number is :',thirdno)

# Assignment 2:##################################################
# Digital Wallet Balance Tracker
# Take the opening wallet balance from the user.
walletbal= int(input(print('enter wallet initial balance :')))
Salarycredit= int(input(print('enter salary credit:')))
# Take a salary credit and add it using
walletbal += Salarycredit
# Take shopping expense and subtract it using
Shoppingexp= int(input(print('enter shopping expence:')))
walletbal-=Shoppingexp
# Take cashback received and add it using
cashbackrcvd= int(input(print('enter Cashback received:')))
walletbal+= cashbackrcvd
# Take electricity bill payment and subtract it using -= .
electricitybill= int(input(print('enter electricity bill expence:')))
walletbal-=electricitybill
print('the final balance i have is:', walletbal)
#Assignment 3:##################################################
# Game Score Updater
startingscore= int(input(print(f'enter Starting Score of Player:')))
# Add points won in Level 1 using
levelonepoints= int(input(print(f'enter points scored in levelone:')))
startingscore += levelonepoints
leveltwopoints= int(input(print(f'enter penalty points lost in leveltwo:')))
startingscore -= leveltwopoints

finalscore = startingscore*2
print('final score of player is:',finalscore)

