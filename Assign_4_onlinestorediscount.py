# A shopper receives a 10% discount if the order is large enough or if they are a premium member.
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# 6. 
# Take order amount.
# Take premium-member status as 
# yes or 
# no .
# If order amount is at least 5000 or the customer is premium, apply a 10% discount.
# Otherwise keep the original bill.
# Print original bill, discount amount and final bill.
# Add an 
# elif : if order amount is at least 10,000 and the member is premium, give 15% instead.
order_amount = float(input("Enter order amount: "))
premium_member = input("Are you a premium member? (yes/no): ")
if order_amount <= 5000 and premium_member == "yes":
    discount = order_amount * 0.10
elif order_amount >= 10000 and premium_member == "yes":
    discount = order_amount * 0.15
else:
    discount = 0

final_bill = order_amount - discount
print(f"Original bill: ${order_amount:.2f}")
print(f"Discount amount: ${discount:.2f}")
print(f"Final bill: ${final_bill:.2f}")