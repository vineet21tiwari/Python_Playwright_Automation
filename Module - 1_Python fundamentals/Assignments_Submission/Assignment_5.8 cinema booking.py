categories = ["comedy", "drama", "action", "horror"]
category = input("Enter movie category: ").lower()
age = int(input("Enter your age: "))
ticket_price = float(input("Enter ticket price: "))
number_of_tickets = int(input("Enter number of tickets: "))
wallet_balance = float(input("Enter wallet balance: "))
total_price = ticket_price * number_of_tickets
if category in categories and wallet_balance >= total_price:
    if category == "horror" and age >= 18:
        print("Booking confirmed.")
    elif category != "horror" and age >= 13:
        print("Booking confirmed.")
    else:
        print("Booking failed: Age restriction not met.")
else:
    if category not in categories:
        print("Booking failed: Invalid category.")
    elif wallet_balance < total_price:
        print("Booking failed: Insufficient funds.")