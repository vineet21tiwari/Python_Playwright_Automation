valid_coupons = ["SAVE10", "SAVE20", "NEWUSER"]
price = float(input("Enter the item price: "))
quantity = int(input("Enter the item quantity: "))
coupon_code = input("Enter the coupon code: ")
membership_type = input("Enter the membership type (regular/premium): ")

subtotal = price * quantity
if subtotal >= 5000 and coupon_code in valid_coupons:
    discount = subtotal * 0.20
elif subtotal >= 3000 or membership_type == "premium":
    discount = subtotal * 0.10
else:
    discount = 0

final_bill = subtotal - discount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount amount: ${discount:.2f}")
print(f"Final bill: ${final_bill:.2f}")

