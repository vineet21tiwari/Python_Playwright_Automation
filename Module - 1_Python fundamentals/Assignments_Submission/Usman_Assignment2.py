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
