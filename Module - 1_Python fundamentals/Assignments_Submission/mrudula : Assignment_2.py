# 1 ======================Digital Wallet Balance Tracker = += -=======================
#   A user starts with a wallet balance, receives money, spends money and gets a cashback.
#   Take the opening wallet balance from the user.
open_Balance= float(input("Enter opening Wallet Balance: "))
 #Take a salary credit and add it using += .
salary = float(input("Enter salary: "))
salary += open_Balance

# Take shopping expense and subtract it using -= .
shopping_exp    = float(input("Enter shopping expense Balance: "))
salary-=shopping_exp
 #Take cashback received and add it using += .
cashback = float(input("Enter cashback Balance: "))
salary +=cashback
 #Take electricity bill payment and subtract it using -= .
electricity_Bill = float(input("Enter electricity Bill: "))
salary-=electricity_Bill
 #Print the balance after every update and the final balance.
print("Final Balance after Expenses:", round(salary,3))
from zoneinfo import available_timezones

 #=====================2 Game Score Updater += -= *======================

#   A player earns points, loses points and then receives a multiplier bonus.
#   Take the player's starting score.
starting_Score = float(input("Enter starting Score: "))
#
#   Add points won in Level 1 using += .
level_1 = float(input("Enter level 1: "))
level_1+=starting_Score
#   Subtract penalty points using -= .
penalty_Score = float(input("Enter penalty Score: "))
penalty_Score-=level_1
#
#   Add Level 2 points using += .
level_2 = float(input("Enter level 2: "))
level_2-=penalty_Score
#   Take a score multiplier such as 2 and update the score using *= .

final_Score = level_2 * 2
#
#   Print the score after each stage and the final score.
print("Final Score:", final_Score)
#
#
#   ==============3 Warehouse Stock Update += -= //= ==============
#   A warehouse tracks stock as items arrive, are sold, and are packed into equal cartons.
#   Take the opening stock quantity.
open_Stock_Qty=int(input("Enter open stock Qty: "))
#   Add newly delivered items using += .
delivered_items=int(input("Enter delivered items: "))
delivered_items+=open_Stock_Qty
print("Number of Items in Stock:", delivered_items)
#   Subtract sold items using -= .
sold_items=int(input("Enter sold items: "))
available_items=delivered_items-sold_items
print("Number of updated Items in Stock Now:", available_items)
#   Subtract damaged items using -= .
damaged_items=int(input("Enter damaged items: "))
available_items-=damaged_items
print("Available Items in Stock after damaged items removed:", available_items)
#   Take items per carton and use a separate variable with //= to calculate complete cartons.
per_carton=int(input("Enter carton: "))
complete_carton= available_items//per_carton
#   Display updated stock and number of complete cartons.
print("Number of Complete Cartons:", complete_carton)

#    =============================Monthly Savings Progress += -= /====================================
#   A student tracks savings after deposits, purchases and an equal sharing calculation.
#   Take the current savings amount.
savings_amount=int(input("Enter initial savings amount: "))
#   Add pocket money using += .
pocket_Money=float(input("Enter pocket Money: "))
savings_amount+=pocket_Money
#   Add gift money using += .
giftMoney=float(input("Enter Gift Money: "))
savings_amount+= giftMoney
print("Initial Savings Amount:",savings_amount)
#   Subtract the cost of a book using -= .
bookCost =float(input("Enter the Cost of the Book:"))
savings_amount-=bookCost
#   Copy the final savings into another variable and use /= to calculate the amount if shared equally among 3 siblings.
final_savings_amount=savings_amount
print("Final Savings Amount:",final_savings_amount)
amount_Shared = final_savings_amount /3
#   Print final savings and equal share.
print("Amount Shared:", round(amount_Shared,3))

#   ================5 Mobile Data Balance Simulator += -= *= /= =======================
#   A user starts with mobile data, buys an add-on, consumes data and then evaluates a promotional multiplier.
#   Take the starting data balance in GB.
start_data_balance=int(input("Enter the starting data balance: "))
#   Add a data add-on using += .
added_data_balance=int(input("Enter the Newly added data balance: "))
availableData=start_data_balance + added_data_balance
print("Available data now:",availableData)
#   Subtract today's usage using -= .
subtracted_data_balance=int(input("Enter the  data balance Used Today: "))
availableData-=subtracted_data_balance
#   Subtract yesterday's pending usage using -= .
yesterday_data_Usage=int(input("Enter yesterday data Used: "))
availableData-=yesterday_data_Usage
print("Available data before promotional data:",availableData)
#   Copy the current balance to a promotional variable and double it using *= .
promotional_data = availableData
promotional_data *=2
#
#   Copy the balance to another variable and use /= to find an equal daily allowance for 5 days.
availableData/=5
daily_allowance=availableData

#   Print original remaining data, promotional data and daily allowance.
print("Available data now:",availableData)
print("Promotional data now:",promotional_data)
print("Daily allowance:",daily_allowance)

#   ===========6 Driving Age Eligibility >= IF-ELSE =============
#   A simple system checks whether a person is old enough for a driving-licence application.
#   Take the person's name and age.
name=input("Enter Person Name:")
age = int(input("Enter Age:"))
#   If age is 18 or above, print "Eligible to apply".
if age >18:
      print("Person is Eligible to Apply for Driving")
#       Otherwise print "Not eligible yet".
else:
     print("Person is Not Eligible to Apply for Driving")
#       Also calculate how many years remain until age 18 and display it only for the not-eligible case.
age -= 18
print("Remaining Age to Apply for Driving:", age)

  #====================7. Pass or Fail Statement IF-Elif=================
  #A student enters marks in three subjects and the program decides the result using the average.
  #Take marks for Maths, Science and English.
math_Marks= float(input("Enter Math Marks:"))
science_Marks= float(input("Enter Science Marks:"))
english_Marks= float(input("Enter English Marks:"))
 #Calculate total and average.
total_Marks= float(math_Marks+science_Marks+english_Marks)
average_marks = round(total_Marks/3,2)
 #If average is 40 or above, print "PASS".
if average_marks >= 40:
     print("Student is PASS")
#  Otherwise print "FAIL".

elif average_marks < 40:
     print("Student is FAIL")
 #Print total and average in both cases.
print("Total Marks:", total_Marks)
print("Average Marks:", average_marks)


#   ===========8 Even or Odd Number Checker % == IF-ELSE ===============
#   Use the modulo operator with a condition to decide whether a number is even or odd.
#   Take an integer from the user.
number=int(input("Enter a number:"))
#  Find the remainder when divided by 2.
remainder=number%2
#  If the remainder is equal to 0, print "Even Number".
if remainder==0:
     print("Entered Number is Even")
#      Otherwise print "Odd Number"
else:
     print("Entered Number is Odd")

  #==============9 Positive, Negative or Zero > < == IF-ELIF-ELSE =============
  #A number can fall into exactly one of three categories.
  #Take a number from the user.
number=int(input("Enter a number:"))
#If the number is greater than 0, print "Positive".
if number >0:
     print("Entered Number is positive:",number)
     final_number= "Number is positive"
#      Else if it is less than 0, print "Negative".
elif number<0:
     print("Entered Number is negative:",number)
     final_number = "Number is Negative"

 #     Otherwise print "Zero".
else:
     print("Entered Number is zero:",number)
     final_number = "Number is zero"

#Print the number together with its category.
print("The final Number is:", number,"and ",final_number)

#   ==========10 Largest of Two Numbers > == IF-ELIF-ELSE============
#   Compare two values and handle the special case where both are equal.
#   Take two numbers from the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#   If the first is greater, print the first as the larger number.
if num1 > num2:
    print("number1 is greater",num1)
#       Else if the second is greater, print the second as the larger number.
elif num1 < num2:
    print("number2 is greater",num2)
#       Otherwise print "Both numbers are equal".
else:
    print("Both Numbers are equal:",num1)

#   =============11 Student Grade Calculator >= ELIF RANGES ==============
#   A school assigns a grade based on percentage.
#   Take percentage from the user.
percentage=float(input("Enter the percentage:"))
#   90 or above: Grade A.
if percentage>=90:
    print("Student Got Grade A",percentage)
#       75 to below 90: Grade B.
elif percentage >= 75 and percentage< 90:
    print("Student Got Grade B",percentage)
#   60 to below 75: Grade C.
elif percentage >=60 and percentage<75:
    print("Student Got Grade C",percentage)
#   40 to below 60: Grade D.
elif percentage >=40 and percentage<60:
    print("Student Got Grade D",percentage)
#   Below 40: Fail.
else:
    print("Student is Fail",percentage)
#   Print the percentage and final grade.

#   ==========12 Movie Ticket Category < >= ELIF ==============
#   A cinema sets ticket prices based on age category.
#   Take customer name and age.
name= input("Enter Customer Name: ")
age= int(input("Enter Customer Age: "))
#   Age below 5: ticket is free.
if age<5:
    print("Congratulations!,", name ,"Your Ticket is Free")
#   Age 5 to 12: ticket price is 150.
elif age >5 and age <=12:
    print(name,"Your Ticket Price is 150")
#   Age 13 to 59: ticket price is 300.
elif age >13 and age <=59:
      print(name,"Your Ticket Price is 300")
#   Age 60 or above: ticket price is 180.
elif age >60:
     print(name,"Your Ticket Price is 180")
#   Print customer name, category and ticket price.


#   ==============13 Simple Login Checker == and IF-ELSE =============
#   A training application has one fixed username and password.
#   Take username and password from the user.
username= input("Enter Username:")
password = input("Enter Password:")
#   Assume the correct username is student and password is python123 .
if username == "student"  and password=="python123":
#      If both username and password are correct, print "Login Successful".
    print("Login Successful.")
#   Otherwise print "Invalid Credentials".
else:
    print("Invalid Credentials")
#   Use the logical operator and to combine the two comparisons.

#   ===========14 Shopping Discount Eligibility >= and / or IF-ELSE ==========
#   A store gives a discount when a customer meets its offer rules.
#   Take purchase amount and membership status as yes or no .
purchase_amount=float(input("Enter purchase amount: "))
membership_status=input("Please Confirm your Membership Status(Yes/No): ")
#   Give a discount if purchase amount is at least 5000 AND the customer is a member.
if purchase_amount > 5000 and membership_status == "Yes":
 #   print ("Discount Applied" or "No Discount".)
      print("Discount Applied for the Purchase Amount",purchase_amount)
#   Then modify the condition so a discount is allowed when purchase amount is at least 8000 OR the customer is a member.

elif purchase_amount > 8000 or membership_status == "Yes":
      print("Discount Applied for the Purchase Amount ",purchase_amount,"on Membership status",membership_status)
#   Run both conditions and compare the results.

#  =========15 Employee Performance Bonus - Master Challenge >= and ELIF NESTED THINKING ===========
#  A company decides bonus level using performance score and attendance.
#  Take employee name, performance score out of 100 and attendance percentage.
name=input("Enter Employee Name: ")
performance_Score=int(input("Enter Performance Score:"))
attendance_percentage=int(input("Enter attendance percentage:"))
#  If score is at least 90 AND attendance is at least 90, print "Excellent - 20% Bonus".
if performance_Score > 90 and attendance_percentage > 90:
     bonus_percentage = 20
     print("Employee Performance is Excellent-20% Bonus",bonus_percentage)
#  Else if score is at least 75 AND attendance is at least 80, print "Good - 10% Bonus".
elif performance_Score >=75 and attendance_percentage >= 80:
     bonus_percentage= 10
     print("Employee Performance is Good - 10% Bonus",bonus_percentage)
#  Else if score is at least 60 AND attendance is at least 75, print "Satisfactory - 5% Bonus".
elif performance_Score >= 60 and attendance_percentage >= 75:
     bonus_percentage = 5
     print("Employee Performance is Satisfactory - 5% Bonus",bonus_percentage)
#  Otherwise print "No Bonus".
else:
     bonus_percentage = 0
     print("Employee Performance is Not Satisfactory- No Bonus")
#  Take monthly salary and calculate the bonus amount using the applicable percentage.#
monthly_salary=float(input("Enter Monthly Salary: "))
annual_salary = (monthly_salary * 12)
bonus= annual_salary * bonus_percentage /100
new_salary= annual_salary +bonus
new_monthly_salary= new_salary / 12
#  Print employee name, category, bonus amount and salary after bonus.
print("Employee Name:",name)
print("Employee Performance Score:",performance_Score)
print("Employee Bonus Amount:",bonus)
print("Employee New Salary:",new_salary)
print("Employee Monthly Salary:",new_monthly_salary)