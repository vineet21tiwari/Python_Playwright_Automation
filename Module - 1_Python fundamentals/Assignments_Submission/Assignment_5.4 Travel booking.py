destinations = ["goa", "delhi", "jaipur", "mumbai"]
destination = input("Enter destination: ")
travellers = int(input("Enter number of travellers: "))
ticket_price = float(input("Enter ticket price per person: "))
wallet_balance = float(input("Enter wallet balance: "))
total_cost = travellers * ticket_price

if destination in destinations:
    if wallet_balance >= total_cost:
        print("Booking successful.")
    else:
        shortage = total_cost - wallet_balance
        print(f"Insufficient balance. You need ${shortage:.2f} more to complete the booking.")
else:
    print("Destination unavailable.")