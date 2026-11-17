# Question:1 Create a list containing five student names and print the complete list.
# Print the first, third and last student using indexing.
# Print the second-last student using negative indexing.
# Print the total number of students using len().
# Replace the second student with a new name and print the updated list

st_names= ['usman','vineeth','mrudula','vakula','rouf']
print(st_names)
print(st_names[::2])
print(st_names[-2])
print(len(st_names))
st_names.pop(1)
st_names.insert(1,'Shireen')
print(st_names)

# Question:2 Create a list with seven daily sales values.
# Print the first three days using slicing.
# Print everything from index 3 to the end using an omitted stop value.
# Print every second sales value using step 2.
# Print the complete list in reverse using slicing

daily_sales=[100.55,250.75,300,425,515]
print(daily_sales[0:3])
print(daily_sales[3:])
print(daily_sales[::2])
print(daily_sales[::-1])

# Question:3Start with a list containing Laptop and Mouse.
# Append Keyboard to the end of the cart.
# Insert Headphones at index 1.
# Replace Mouse with Wireless Mouse using list indexing.
# Print the final cart and total number of products

comp_spare=['laptop','mouse']
comp_spare.append('keyboard')
print(comp_spare)
comp_spare.insert(1,'headphones')
print(comp_spare)
comp_spare.pop(2,)
comp_spare.insert(2,'wirelessmouse')
print(comp_spare,'number of products is:',len(comp_spare))


# Question:4  Create frontend = ["HTML", "CSS"] and backend = ["Python", "Java"].
# Use extend() to add all backend courses into the frontend list.
# Print the merged list and its length.
# Create a fresh ["HTML", "CSS"] list and append the entire backend list once.
# Print both results and write one comment explaining the difference between append() and extend()

frontend =["HTML", "CSS"]
backend = ["Python", "Java"]
frontend.extend(backend)
print(frontend,'number of courses is:',len(frontend))
frontend1 =["HTML", "CSS"]
frontend1.append(backend[:])
print(frontend1,'number of courses is:',len(frontend1))
print('The difference between extend and append is extend will add all elements as a seperate element'
      'and gives a index for each element but append will add all the elements as one list and for'
      'all elements it gives same index')

# Question:5  Create a list with five product names.
# Remove one product by value using remove().
# Remove the item at index 1 using pop(1) and store the removed value.
# Print the removed value and the remaining inventory.
# Finally use clear() and print the empty list.
comp_products=['laptop','mouse','monitor','keyboard','motherboard']
comp_products.remove('laptop')
str=comp_products.pop(1)
print(str,comp_products,'number of products is:',len(comp_products))


# # Question:6 Create users = ["aman", "rahul", "priya", "neha"].
# Take a new username from the user and normalize it to lowercase.
# If it already exists, print "Username already exists".
# Otherwise append it and print "Username registered".
# If the username exists after processing, print its index using index()

users = ["aman", "rahul", "priya", "neha"]
new_user= input("Enter new username: ")
new_user= new_user.lower()

if new_user in users:
      print("Username already exists")
else:
      users.append(new_user)
      print(users,'new user is at posiyion:',users.index(new_user))

# Question:7  Create a list containing at least ten votes with repeated values.
# Use count() to print the votes received by Sports, Coding and Music.
# Check whether "Dance" appears in the vote list.
# Print which option received the most votes using the counts you calculated.
# Print the total number of votes using len()
# i dont like it..
# Question:8 Create a list with at least six different scores.
# Print the highest and lowest scores using max() and min().
# Sort the list in ascending order and print it.
# Sort it again in descending order using sort(reverse=True).
# Use reverse() once and explain in a comment how reverse() differs from sort()

scores=[6,8,20,56,34,94,37,4]
print('Highest score is:',max(scores),'Lowest score is:',min(scores))
print(sorted(scores)[:],sorted(scores)[::-1])

# Question:9 .
# Use marks = [76, 35, 89, 42, 28, 91, 67].
# Loop through the list and calculate the total manually using an accumulator.
# Calculate the average using the total and len(marks).
# Count passed students (marks >= 40) and failed students.
# Print the highest, lowest and all marks greater than the class average

marks = [76, 35, 89, 42, 28, 91, 67]
i=len(marks)-1
m=0
total=0
for j in marks:
      i=i-1
      total=total+j
      if total>0:
            print('mark is:',marks[i],'total is:',total)
      else:print('total is zero:')

# Question:10 Use transactions = [1200, -500, 2300, 0, 850, -100, 3000].
# Loop through the list and skip negative values using continue.
# Ignore zero values as well.
# Calculate total valid sales and count valid transactions.
# Print the largest valid transaction without including invalid values.

transactions = [1200, -500, 2300, 0, 850, -100, 3000]
i=len(transactions)-1
cnt=0
total1=0
print(i)
for t in transactions:
      i = i - 1

      total1 = total1 + t
      if total1 > 0 and transactions[i] > 0:
            print('mark is:', transactions[i], 'total is:', total1)
            cnt+=1
      else:
            print('total is zero:')
      continue
print('number of valid transactions are:',cnt)
print('valid maximum Transaction is:',max(transactions))

# Question:11 Use numbers = [12, -5, 7, 20, -8, 15, 0, 18, 25].
# Count even and odd numbers, excluding zero from the odd count.
# Count positive and negative numbers.
# Calculate the sum of numbers divisible by 5.
# Print only the positive even numbers

evn_cnt=0
odd_cnt=0
postve_cnt=0
neg_cnt=0
sum_dvd5=0
numbers = [12, -5, 7, 20, -8, 15, 0, 18, 25]
for n in numbers:
      if n%2!=0 and n>0:
            odd_cnt = odd_cnt + 1
      else:
            evn_cnt = evn_cnt + 1
            if n>0 and n%5==0:
                sum_dvd5 = sum_dvd5 + 1
          elif n>0:
                postve_cnt = postve_cnt + 1
          elif n<0:
                neg_cnt = neg_cnt + 1

      print(evn_cnt,odd_cnt,postve_cnt,neg_cnt)

# Question:12  Create a list of at least eight numeric product IDs.
# Take a product ID to search from the user.
# Use for i in range(len(list)) so you can access both index and value.
# When the ID is found, print its index and stop immediately using break.
# If it is not found, print a clear "Product not found" message

product_ids = [12, 5, 7, 20, 8, 15, 70, 18, 25]
i=int(input(print('Enter a product_id:')))
for j in range(0,len(product_ids)):
    print(j,product_ids[j])
    if i==product_ids[j]:
        print('found your product and it is in this position is:',j,product_ids[j])
        break
    else:continue
print('your product not found in this perticular list sorry:')

# Question:13  Start with an empty prices list.
# Use a for loop to take exactly five prices from the user and append each one.
# Print the completed list, total and average price.
# Print the highest and lowest price.
# Count how many products cost more than the average

price_list=[]
for j in range(0,4):
    # k=int(input('please enter a price:'))
    price_list.append(int(input('please enter a price:')))
    sum_price=sum(price_list)
    avg_price=sum_price/len(price_list)
print('the sum of the prices is',sum_price)
print('your average price is ',avg_price)

# # Question:14
# Use names = ["Aman", "Priya", "Aman", "Rahul", "Priya", "Neha"].
# Create an empty unique_names list.
# Loop through names and append a name only when it is not already in unique_names.
# Print the cleaned list and number of unique customers.
# Do not use set() for this question

names = ["Aman", "Priya", "Aman", "Rahul", "Priya", "Neha"]
unique_names = []
i=0
for name in names:
    name = names[i]
    i+=1
    if name not in unique_names:
        unique_names.append(name)
print(unique_names,'number of unique names are:',len(unique_names),'\n')

# # Question:15   Take a sentence from the user and convert it into a word list using split().
# Print the word list and total number of words.
# Loop through the list and find the longest word manually.
# Count how many words have more than 5 characters.
# Sort the words alphabetically and print the final list

sentence=input(print('please enter a story:'))
words=sentence.split()
print(words)
i=0
each_word=[]
chars_five_above=[]
each_word_ln=[]
for i in range(len(words)):
    each_word.append(words[i])
    each_word_ln.append(len(words[i]))
    if(len(words[i])>=5):
        chars_five_above.append(words[i])
print(each_word,'/n')
print(each_word_ln)
bw_length=max(each_word_ln)
biggest_word_idx= each_word_ln[bw_length]
print(biggest_word_idx,max(each_word_ln))
