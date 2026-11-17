#=========================1.Student Roster Inspector==============================
#A trainer stores five student names in one list and wants a quick summary before starting class.
#Your program must:
# a.Create a list containing five student names and print the complete list.
from os import remove
from string import ascii_uppercase

student_name=["student1","student2","student3","student4","student5"]
print(student_name)
# b.Print the first, third and last student using indexing.
print(student_name[::2])
# c.Print the second-last student using negative indexing.
print(student_name[-2])
# d.Print the total number of students using len().
print("Total Number of Students:",len(student_name))
# e.Replace the second student with a new name and print the updated list
student_name[1]="Student_new"
print(student_name)

#============================2.Weekly Sales Slice========================================
#A shop stores sales for seven days in a list. The manager wants different views of the same weekly data.
#Your program must:
# a.Create a list with seven daily sales values.
daily_sales_value=[120,150,200,175,250,300,225]
# b.Print the first three days using slicing.
print(daily_sales_value[0:3])
# c.Print everything from index 3 to the end using an omitted stop value.
print(daily_sales_value[3:])
# d.Print every second sales value using step 2.
print(daily_sales_value[0::2])
# e.Print the complete list in reverse using slicing
print(daily_sales_value[::-1])

#==========================3.Shopping Cart Builder============================================
#An online cart starts with two products. The customer adds products and changes one selection before checkout.
#Your program must:
#a.Start with a list containing Laptop and Mouse.
customer_list=['Laptop','Mouse']
print(customer_list)
# b.Append Keyboard to the end of the cart.
customer_list.append("Keyboard")
print(customer_list)
# c.Insert Headphones at index 1.
customer_list.insert(1,"Headphones")
print(customer_list)
# d.Replace Mouse with Wireless Mouse using list indexing.
customer_list[2]="Wireless Mouse"
# e.Print the final cart and total number of products
print(customer_list)
print("Total Products",len(customer_list))

#============================4.Course Catalog Merger==========================================
#A training portal has separate frontend and backend course lists that need to be combined.
#Your program must:
#a.Create frontend = ["HTML", "CSS"] and backend = ["Python", "Java"].
frontend = ["HTML", "CSS"]
backend = ["Python", "Java"]
# b.Use extend() to add all backend courses into the frontend list.
frontend.extend(backend)
# c.Print the merged list and its length.
print(frontend)
print("Length of Frontend Courses are:",len(frontend))
# d.Create a fresh ["HTML", "CSS"] list and append the entire backend list once.
new_backend = ["HTML", "CSS"]
new_backend.append(backend)
# e.Print both results and write one comment explaining the difference between append() and extend()
print(frontend)
print(new_backend)
print("append()-- Adds new value at the end of the list whereas extend adds every element into existing list")

#==================================5.Inventory Removal Desk================================================================
#A small store updates inventory when items are sold, discontinued or completely reset for stock-taking.
# Your program must:
# a.Create a list with five product names.
products=['Salt','Sugar','Coffee','Tea','Honey']
# b.Remove one product by value using remove().
products.remove("Sugar")
print(products)
# c.Remove the item at index 1 using pop(1) and store the removed value.
removed_products=products.pop(1)
print(removed_products)
# d.Print the removed value and the remaining inventory.
print("Updated Inventory",products)
# e.Finally use clear() and print the empty list.
products.clear()
print("empty list",products)

#==============================6.Username Registration Check======================================================
#A website keeps a list of existing usernames and must prevent duplicate registrations.
#Your program must:
# a.Create users = ["aman", "rahul", "priya", "neha"].
users = ["aman", "rahul", "priya", "neha"]
# b.Take a new username from the user and normalize it to lowercase.
new_users = input("Enter new users: ")
new_user=new_users.lower()
print(new_user)
# c.If it already exists, print "Username already exists".
if new_user in users:
    print("Entered New User Already Exists")
else:
# d.Otherwise append it and print "Username registered".
    users.append(new_user)
    print("Username registered",users)
# e.If the username exists after processing, print its index using index()
print(users.index(new_user))


#================================7.Class Vote Counter========================================================
#Students vote for one of three activities: Sports, Coding or Music. Votes are stored in a list.
#Your program must:
# a.Create a list containing at least ten votes with repeated values.
votes_list=["Sports", "Coding", "Music", "Sports", "Coding","Sports", "Music", "Coding", "Sports", "Music"]
sport_count=0
music_count=0
coding_count=0
# b.Use count() to print the votes received by Sports, Coding and Music.
for vote in votes_list:
    if "Sports" in votes_list:
        sport_count=votes_list.count("Sports")
    if "Music" in votes_list:
        music_count=votes_list.count("Music")
    if "Coding" in votes_list:
        coding_count=votes_list.count("Coding")
# c.Check whether "Dance" appears in the vote list.
if "Dance" in votes_list:
    print("Dance is listed in the List")
else:
    print("Dance is not listed in the List")
# d.Print which option received the most votes using the counts you calculated.
print(sport_count)
print(music_count)
print(coding_count)
# e.Print the total number of votes using len()
print(len(votes_list))

#=======================8.Leaderboard Organizer=================================
#A game stores player scores in a list and needs ascending and descending leaderboard views.
# Your program must:
# a.Create a list with at least six different scores.
scores = [85, 92, 78, 95, 88, 76]
# b.Print the highest and lowest scores using max() and min().
print(max(scores))
print(min(scores))
min_count=0
max_count=0
# c.Sort the list in ascending order and print it.
for score in scores:
    if score > max_count:
        max_count = score
    if score > min_count:
        min_count = score
# d.Sort it again in descending order using sort(reverse=True).
scores.sort(reverse=True)
print("Descending Order",scores)
# e.Use reverse() once and explain in a comment how reverse() differs from sort()
scores.reverse()
print("Reversed Order",scores)
print("reverse will display from right to left whereas sort id display in ascending/descending order")

#====================9.Exam Result Analyzer================================================
#A teacher stores class marks in a list and wants a simple result summary without entering each mark separately.
#Your program must:
# a.Use marks = [76, 35, 89, 42, 28, 91, 67].
marks = [76, 35, 89, 42, 28, 91, 67]
total=0
pass_count=0
fail_count=0
# b.Loop through the list and calculate the total manually using an accumulator.
for mark in marks:
    total+=mark
# c.Calculate the average using the total and len(marks).
average=total/len(marks)
# d.Count passed students (marks >= 40) and failed students.
for mark in marks:
    if mark>=40:
        pass_count+=1
    else:
        fail_count+=1
# e.Print the highest, lowest and all marks greater than the class average
print("Highest Marks:",max(marks))
print("Lowest Marks:",min(marks))
print("Total Marks",total)
print("Average Marks",round(average,3))
print("Pass Count",pass_count)
print("Fail Count",fail_count)
for mark in marks:
    if mark>average:
        print("Mark",mark)

#=============================10.Transaction Cleaner===========================
#A payment system receives transaction values where negative numbers are invalid and zero means no payment.
#Your program must:
# a.Use transactions = [1200, -500, 2300, 0, 850, -100, 3000].
transactions = [1200, -500, 2300, 0, 850, -100, 3000]
count=0
valid_sales=0
# b.Loop through the list and skip negative values using continue.
for transaction in transactions:
    if transaction<=0:
        continue
    valid_sales+=transaction
    count+=1
# c.Ignore zero values as well.
# d.Calculate total valid sales and count valid transactions.
# e.Print the largest valid transaction without including invalid values
print("Maximum Transaction",max(transactions))
print("Valid Sales",valid_sales)
print("Total count of Transactions",count)

# =======================11.Number Lab============================
# A data exercise stores mixed positive and negative integers and asks for several classifications in one pass.
# Your program must:
# a.Use numbers = [12, -5, 7, 20, -8, 15, 0, 18, 25].
numbers = [12, -5, 7, 20, -8, 15, 0, 18, 25]
# b.Count even and odd numbers, excluding zero from the odd count.
even_num = 0
odd_num = 0
positive_num = 0
negative_num = 0
sum_of_5 = 0
for num in numbers:
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    # c.Count positive and negative numbers.
    if num > 0:
        positive_num += 1
    elif num < 0:
        negative_num += 1
    # d.Calculate the sum of numbers divisible by 5.
    if num % 5 == 0:
        sum_of_5 += num

    # e.Print only the positive even numbers
    if num > 0 and num % 2 == 0:
        print("Number", num, "is positive and it is even number:", num)
print("Even:", even_num)
print("Odd:", odd_num)
print("Positive:", positive_num)
print("Negative:", negative_num)
print("Sum divisible by 5:", sum_of_5)

#=============================12.Search and Stop==================================================
#A warehouse scans product IDs in order and wants to stop scanning as soon as the requested ID is found.
#Your program must:
# a.Create a list of at least eight numeric product IDs.
product_id=[12,34,56,67,89,68,45,23]
# b.Take a product ID to search from the user.
user_id = int(input("Enter User ID:"))
product_found=False
# c.Use for i in range(len(list)) so you can access both index and value.
for i in range(len(product_id)):
    if product_id[i]==user_id:
# d.When the ID is found, print its index and stop immediately using break.
        print("Product ID:",product_id[i])
        print("index",i)
        break
    else:
        # e.If it is not found, print a clear "Product not found" message
        print("Product not found")


# ===========================13.Five-Item Price Collector==============================================
# A billing program asks the cashier to enter five product prices and stores them for later analysis.
# Your program must:
# a.Start with an empty prices list.
price_list = []
total_price = 0
average_price=0
product_cost=0
# b.Use a for loop to take exactly five prices from the user and append each one.
for price in range(5):
    price = int(input("price:"))
    price_list.append(price)
    total_price += price
    average_price = total_price/5
# c.Print the completed list, total and average price.
print(price_list)
print(total_price)
print(average_price)
# d.Print the highest and lowest price.
print(max(price_list))
print(min(price_list))
# e.Count how many products cost more than the average
for price in price_list:
    if price > average_price:
        product_cost += 1
print(product_cost)








































