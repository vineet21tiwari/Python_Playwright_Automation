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

