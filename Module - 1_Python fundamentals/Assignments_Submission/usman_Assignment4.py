==============3 Warehouse Stock Update += -= //= ==============
#   A warehouse tracks stock as items arrive, are sold, and are packed into equal cartons.
#   Take the opening stock quantity.
open_Stock_Qty=int(input("Enter open stock Qty: "))
#   Add newly delivered items using += .
delivered_items=int(input("Enter delivered items: "))
open_Stock_Qty+=delivered_items
print("Number of Items in Stock:", open_Stock_Qty)
#   Subtract sold items using -= .
sold_items=int(input("Enter sold items: "))
open_Stock_Qty-=sold_items
print("Number of updated Items in Stock Now:", open_Stock_Qty)
#   Subtract damaged items using -= .
damaged_items=int(input("Enter damaged items: "))
open_Stock_Qty-=damaged_items
print("Available Items in Stock after damaged items removed:", open_Stock_Qty)
#   Take items per carton and use a separate variable with //= to calculate complete cartons.
per_carton=int(input("Enter carton: "))
complete_carton= open_Stock_Qty//per_carton
#   Display updated stock and number of complete cartons.
print("Number of Complete Cartons:", complete_carton)