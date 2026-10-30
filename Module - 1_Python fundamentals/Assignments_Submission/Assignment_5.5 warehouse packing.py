restricted_items = ["chemical", "battery", "aerosol"]
product_name = input("Enter product name: ").lower()
total_quantity = int(input("Enter total quantity: "))
box_capacity = int(input("Enter box capacity: "))

if product_name in restricted_items:
    print("Shipment blocked.")
elif total_quantity <= 0 or box_capacity <= 0:
    print("Invalid input.")
else:
    complete_boxes = total_quantity // box_capacity
    leftover_items = total_quantity % box_capacity
    print(f"Complete boxes: {complete_boxes}")
    print(f"Leftover items: {leftover_items}")