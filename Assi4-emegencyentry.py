# A restricted facility normally requires an access card, but emergency staff are also allowed entry.
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# Take whether the person has a valid access card.
# Take the person's role: employee, doctor, firefighter or visitor.
# Allow entry if the access card is valid or role is doctor or firefighter.
# Otherwise print Entry denied.
# Print the exact reason for the granted access in a separate message.
AccessCard = input("Do you have a valid access card? (yes/no): ").strip().lower()
Role = input("What is your role? (employee/doctor/firefighter/visitor): ").strip().lower()  

if AccessCard == "yes" or Role in ["doctor", "firefighter"]:
    print("Entry granted.")
    if AccessCard == "yes":
        print("Reason: Valid access card.")
    else:
        print("Reason: Emergency staff member.")
else:
    print("Entry denied.")  