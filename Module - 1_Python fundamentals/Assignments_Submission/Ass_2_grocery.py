# rice_prive = float(input("Enter the rice price: "))
# rice_quantity = int(input("Enter the rice quantity: "))

# milk_price = float(input("Enter the milk price: "))
# milk_quantity = int(input("Enter the milk quantity: "))

# oil_price = float(input("Enter the oil price: "))
# oil_quantity = int(input("Enter the oil quantity: "))

# rice_cost = rice_prive * rice_quantity
# milk_cost = milk_price * milk_quantity  
# oil_cost = oil_price * oil_quantity

# subtotal = rice_cost + milk_cost + oil_cost

# Discount = float(input("Enter the discount amount  : "))
# after_discount = subtotal - Discount

# delivery_fee = float(input("Enter the delivery fee: "))    
# final_price = after_discount + delivery_fee

# Family_members = int(input("Enter the number of family members: "))
# final_price_per_member = final_price / Family_members
# cost_per_member = round(final_price_per_member, 2)  

# print("-------Grocery Bill-------")
# print("Rice Cost: $", rice_cost)
# print("Milk Cost: $", milk_cost)
# print("Oil Cost: $", oil_cost)
# print("Subtotal: $", subtotal)
# print("Discount: $", Discount)
# print("After Discount: $", after_discount)
# print("Delivery Fee: $", delivery_fee)
# print("Final Price: $", final_price)    
# print("Cost per Family Member: $", cost_per_member)
#######################################################################3
#q4
one_way_distance = float(input("Enter the one-way distance in kilometers: "))
mileage = float(input("Enter the mileage in kilometers per liter: "))
fuel_price = float(input("Enter the fuel price per liter: "))
travellers = int(input("Enter the number of travelers: "))
round_trip_distance = one_way_distance * 2
fuel_needed = round_trip_distance / mileage
total_fuel_cost = fuel_needed * fuel_price
toll_fee = float(input("Enter the toll fee: "))
parking_fee = float(input("Enter the parking fee: "))
total_trip_cost = total_fuel_cost + toll_fee + parking_fee
cost_per_traveler = total_trip_cost / travellers
print("-------Road Trip summary-------")        
print("round trip distance: ", round_trip_distance, "km")
print("Fuel needed: ", fuel_needed, "liters")
print("Total fuel cost: $", total_fuel_cost)
print("Toll fee: $", toll_fee)
print("Parking fee: $", parking_fee)
print("Total trip cost: $", round(total_trip_cost, 2))
print("Cost per traveler: $", round(cost_per_traveler, 2))
################################################################
total_candy=int(input("Enter the total number of candies: "))
num_students=int(input("Enter the number of students: "))
each_student_candies=total_candy//num_students
remaining_candies=total_candy%num_students  
extra_candies_boxes=int(input("Enter the number of extra candies boxes: "))
candies_per_box=extra_candies_boxes//num_students


print("Each student gets:", each_student_candies, "candies")
print("Remaining candies:", remaining_candies)
print("Candies per box:", candies_per_box)      
