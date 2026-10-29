# An employee can enter a secure dashboard only when both username and PIN are correct.
# 1. 

# 6. 
# Store a correct username and correct PIN in variables.
# Take username and PIN from the user.
# If both match, print Login successful.
# Otherwise print Invalid credentials.
# Add a second condition requiring 
# account_active == True .
# If credentials are correct but the account is inactive, print a separate message using 

username = "admin"
pin = "1234"    
print=input("Enter username: ")
pin_input = input("Enter PIN: ")
if print == username and pin_input == pin:
    print("Login successful.")  
else:
    print("Invalid credentials.")

    account_active = True
    if print == username and pin_input == pin and account_active:
        print("Login successful.")
    elif print == username and pin_input == pin and not account_active:
        print("Account is inactive. Please contact support.")

