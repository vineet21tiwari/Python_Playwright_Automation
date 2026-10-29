# An e-commerce app decides whether delivery is free, discounted or charged normally.
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# Questions 07-08
# Take cart value and membership status.
# Give free delivery if cart value is at least 999 or the user is a premium member.
# If cart value is between 499 and 998 and the user is not premium, charge a reduced delivery fee of 40.
# Otherwise charge a normal delivery fee of 80.
# Print cart value, delivery fee and final payable amount.
cart_value = float(input("Enter the cart value: "))
membership_status = input("Are you a premium member? (yes/no): ").strip().lower()
if cart_value >= 999 or membership_status == "yes":
    delivery_fee = 0        
elif 499 <= cart_value < 999 and membership_status == "no":
    delivery_fee = 40   
else:   
    delivery_fee = 80   
print("Cart value: ", cart_value)
print("Delivery fee: ", delivery_fee)
final_amount = cart_value + delivery_fee
print("Final payable amount: ", final_amount)
