# A ride is allowed only when the visitor meets both age and height requirements.
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# Take visitor age and height in centimetres.
# Allow the ride only when age is at least 12 and height is at least 140 cm.
# If age qualifies but height does not, print Height requirement not met.
# If height qualifies but age does not, print Age requirement not met.
# Otherwise print Ride allowed only for the fully valid case
visitor_age = int(input("Enter visitor age: "))
visitor_height = float(input("Enter visitor height in cm: "))
if visitor_age >= 12 and visitor_height >= 140:
    print("Ride allowed.")
elif visitor_age >= 12 and visitor_height < 140:
    print("Height requirement not met.")
elif visitor_age < 12 and visitor_height >= 140:
    print("Age requirement not met.")
else:
    print("Both requirements not met.") 