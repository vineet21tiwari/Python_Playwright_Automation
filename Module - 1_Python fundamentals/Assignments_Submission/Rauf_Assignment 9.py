#9.1
Student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Complete list of students:", Student_names)
print("First student:", Student_names[0])
print("Third student:", Student_names[2])
print("Last student:", Student_names[4])
print("Second-last student:", Student_names[-2])
print("Total number of students:", len(Student_names))
Student_names[1] = "Frank"
print("Updated list of students:", Student_names)

#9.2
daily_sales = [150, 200, 175, 300, 250, 400, 350]
print("First three days sales:", daily_sales[:3])
print("Days 4 to 7 sales:", daily_sales[3:7])
print("Every second day sales:", daily_sales[::2])
print("Sales in reverse order:", daily_sales[::-1])

#9.3
cart = ["Laptop", "Mouse"]
cart.append("Keyboard")
cart.insert(1, "Headphones")
cart[1] = "Wireless Mouse"
print("Final cart:", cart)
print("Total number of products:", len(cart))

#9.4
frontend = ["HTML", "CSS"]
backend = ["Python", "Java"]
frontend.extend(backend)
print("Merged list:", frontend)
print("Length of merged list:", len(frontend))
frontend = ["HTML", "CSS"]
frontend.append(backend)
print("List with appended backend:", frontend)

#9.5
products = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
products.remove("Bananas")
removed_product = products.pop(1)
print("Removed product:", removed_product)
print("Remaining inventory:", products)
products.clear()
print("Empty list:", products)

#9.6
users = ["aman", "rahul", "priya", "neha"]
new_username = input("Enter a new username: ").strip().lower()
if new_username in users:
    print("Username already exists")
else:
    users.append(new_username)
    print("Username registered")
if new_username in users:
    print("Index of the username:", users.index(new_username))

#9.7
votes = ["Sports", "Coding", "Music", "Sports", "Coding", "Music", "Sports", "Coding", "Music", "Sports"]
print("Sports votes:", votes.count("Sports"))
print("Coding votes:", votes.count("Coding"))
print("Music votes:", votes.count("Music"))
if "Dance" in votes:
    print("Dance appears in the vote list.")
else:
    print("Dance does not appear in the vote list.")

max_votes = max(votes.count("Sports"), votes.count("Coding"), votes.count("Music"))
if max_votes == votes.count("Sports"):
    print("Sports received the most votes.")
elif max_votes == votes.count("Coding"):
    print("Coding received the most votes.")
else:
    print("Music received the most votes.")

#9.8
leaderboard = [250, 400, 150, 300, 500, 350]
print("Highest score:", max(leaderboard))
print("Lowest score:", min(leaderboard))
leaderboard.sort()
print("Leaderboard in ascending order:", leaderboard)
leaderboard.sort(reverse=True)
print("Leaderboard in descending order:", leaderboard)
leaderboard.reverse()
print("Leaderboard after reverse():", leaderboard)
# Note: reverse() simply reverses the current order of the list, while sort(reverse=True) sorts the list in descending order based on the values.

#9.9
marks = [76, 35, 89, 42, 28, 91, 67]
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
passed = 0
failed = 0
for mark in marks:
    if mark >= 40:
        passed += 1
    else:
        failed += 1
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Class average:", average)
print("Passed students:", passed)
print("Failed students:", failed)

#9.10
transactions = [1200, -500, 2300, 0, 850, -100, 3000]
total_sales = 0
valid_transactions_count = 0
largest_valid_transaction = None

for transaction in transactions:
    if transaction < 0 or transaction == 0:
        continue
    total_sales += transaction
    valid_transactions_count += 1
    if largest_valid_transaction is None or transaction > largest_valid_transaction:
        largest_valid_transaction = transaction

print("Total valid sales:", total_sales)
print("Count of valid transactions:", valid_transactions_count)
print("Largest valid transaction:", largest_valid_transaction)

#9.11
numbers = [12, -5, 7, 20, -8, 15, 0, 18, 25]
even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0
sum_divisible_by_5 = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        if n != 0:
            odd_count += 1
    if n > 0:
        positive_count += 1
    elif n < 0:
        negative_count += 1
    if n % 5 == 0:
        sum_divisible_by_5 += n

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Sum of numbers divisible by 5:", sum_divisible_by_5)

print("Positive even numbers:")
for n in numbers:
    if n > 0 and n % 2 == 0:
        print(n)
#9.12
    product_ids = [101, 202, 303, 404, 505, 606, 707, 808]
    search_id = int(input("Enter the product ID to search: "))
    found = False

    for i in range(len(product_ids)):
        if product_ids[i] == search_id:
            print(f"Product found at index {i}")
            found = True
            break

    if not found:
        print("Product not found")

#9.13
    prices = []
    for i in range(5):
        price = float(input(f"Enter price for product {i + 1}: "))
        prices.append(price)

    total = sum(prices)
    average = total / len(prices) if prices else 0

    print("Completed list:", prices)
    print("Total price:", total)
    print("Average price:", average)
    print("Highest price:", max(prices))
    print("Lowest price:", min(prices))

    count_above_average = sum(1 for price in prices if price > average)
    print("Number of products costing more than the average:", count_above_average)

    #9.14
    names = ["Aman", "Priya", "Aman", "Rahul", "Priya", "Neha"]
    unique_names = []

    for name in names:
        if name not in unique_names:
            unique_names.append(name)

    print("Cleaned list:", unique_names)
    print("Number of unique customers:", len(unique_names))

    #9.15
    sentence = input("Enter a sentence: ").strip()

    # 1. Convert the sentence into a word list
    words = sentence.split()

    # 2. Print the word list and total number of words
    print("Word list:", words)
    print("Total number of words:", len(words))

    if len(words) == 0:
        print("No words entered.")
    else:
        # 3. Find the longest word manually
        longest_word = words[0]
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
        print("Longest word:", longest_word, f"({len(longest_word)} characters)")

        # 4. Count words with more than 5 characters
        long_word_count = 0
        for word in words:
            if len(word) > 5:
                long_word_count += 1
        print("Words with more than 5 characters:", long_word_count)

        # 5. Sort the words alphabetically (case-insensitive) and print
        sorted_words = sorted(words, key=str.lower)
        print("Sorted words:", sorted_words)
#9.16
# a. Create the nested list
students = [["Aman", 80], ["Rahul", 65], ["Priya", 92]]

# b. First student's name and marks using nested indexing
print("First student name:", students[0][0])
print("First student marks:", students[0][1])

# c. Loop through all records and print each student with marks
print("\nAll students:")
for student in students:
    print(f"{student[0]} - {student[1]}")

# d. Count students who scored at least 75
count_75_plus = 0
for student in students:
    if student[1] >= 75:
        count_75_plus += 1
print("\nStudents with marks >= 75:", count_75_plus)

# e. Find the student with the highest marks
top_student = students[0]
for student in students:
    if student[1] > top_student[1]:
        top_student = student
print("Highest marks:", top_student[0], f"({top_student[1]})")

#9.17
# a. Start with an empty cart and add five products using append()
cart = []
while len(cart) < 5:
    product = input(f"Enter product {len(cart) + 1} of 5: ").strip().lower()
    if product == "":
        print("Product name cannot be empty.")
    else:
        cart.append(product)

# b. Print the cart with item numbers using range(len(cart))
print("\nYour cart:")
for i in range(len(cart)):
    print(f"{i + 1}. {cart[i]}")

# c. Search for a product
search_item = input("\nEnter a product to search: ").strip().lower()
if search_item in cart:
    print(f"'{search_item}' found at index {cart.index(search_item)}.")
else:
    print(f"'{search_item}' is not in the cart.")

# d. Remove a product only if it exists
remove_item = input("\nEnter a product to remove: ").strip().lower()
if remove_item in cart:
    cart.remove(remove_item)
    print(f"'{remove_item}' removed.")
else:
    print(f"'{remove_item}' is not in the cart, nothing removed.")

# e. Remove duplicates into a new list without using set()
unique_cart = []
for item in cart:
    if item not in unique_cart:
        unique_cart.append(item)

# f. Sort the cleaned cart and print count, first and last item
unique_cart.sort()
print("\nFinal cart:", unique_cart)
print("Item count:", len(unique_cart))
if len(unique_cart) > 0:
    print("First item:", unique_cart[0])
    print("Last item:", unique_cart[-1])