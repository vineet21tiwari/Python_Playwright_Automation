service_zones = ["madhapur", "gachibowli", "kondapur", "hitech city"]
delivery_area = input("Enter delivery area: ").lower()
food_total = float(input("Enter food total amount: "))
delivery_charge = float(input("Enter delivery charge: "))
premium_member = input("Are you a premium member? (yes/no): ").lower()

if delivery_area in service_zones and food_total > 0:
    if food_total >= 1000 or premium_member == "yes":
        print("Serviceable.")
        print("Free delivery applied.")
        final_amount = food_total
    else:
        print("Serviceable.")
        print(f"Delivery charge applied: ${delivery_charge:.2f}")
        final_amount = food_total + delivery_charge
else:
    print("Not serviceable.")

print(f"Final payable amount: ${final_amount:.2f}")