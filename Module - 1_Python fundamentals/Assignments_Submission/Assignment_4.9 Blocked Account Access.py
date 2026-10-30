# A user may access an application only if the password is correct and the account is not blocked.
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# 6. 
# Store the correct password in a variable.
# Take the user's password.
# Take blocked status as 
# True or 
# False in the program.
# Allow access when the password matches and
# not is_blocked .
# If password is correct but the account is blocked, print Contact support.
# Otherwise print Incorrect password.
x="password123"
user_password = input("Enter your password: ")
is_blocked = bool(input("Is your account blocked? (True/False): "))
print("-------Access Summary-------")
if user_password == x and not is_blocked:
    print("Access granted.")    
elif user_password == x and is_blocked:
        print("Contact support.")
else:
        print("Incorrect password.")
    