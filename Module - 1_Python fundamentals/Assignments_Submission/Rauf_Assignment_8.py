#8.1
badge_text = input("Enter the badge text: ")
print("Total characters: {len(badge_text)}")
print("First character: {badge_text[0]}")
print("Last character: {badge_text[-1]}")
print("Second character: {badge_text[1]}")
print("Second-last character: {badge_text[-2]}")
print("Course prefix: {badge_text[:2]}")
print("Last six characters: {badge_text[-6:]}")
print("First and last characters are the same: {badge_text[0] == badge_text[-1]}")
#8.2
tracking_code = "HYD2026EXPRESS"
# Print the first three characters (start=0, stop=3, step=1)
print(tracking_code[:3])  # Effective start=0, stop=3, step=1
# Print everything from index 3 to the end (start=3, stop=len(tracking_code), step=1)
print(tracking_code[3:])  # Effective start=3, stop=len(tracking_code), step=1
# Print the complete code (start=0, stop=len(tracking_code), step=1)
print(tracking_code[:])  # Effective start=0, stop=len(tracking_code), step=1
# Print characters from index 3 up to, but not including, index 7 (start=3, stop=7, step=1)
print(tracking_code[3:7])  # Effective start=3, stop=7, step=1

#8.3
token = "A1B2C3D4E5F6"
# Print every second character starting from the beginning (start=0, stop=len(token), step=2)
print(token[::2])  # Effective start=0, stop=len(token), step=2
# Print every second character starting from index 1 (start=1, stop=len(token), step=2)
print(token[1::2])  # Effective start=1, stop=len(token), step=2
# Print the token from index 2 to index 10 using a step of 2 (start=2, stop=10, step=2)
print(token[2:10:2])  # Effective start=2, stop=10, step=2
# Print the token in reverse (start=len(token)-1, stop=-1, step=-1)
print(token[::-1])  # Effective start=len(token)-1, stop=-1, step=-1
# Print the reversed token while taking every second character (start=len(token)-1, stop=-1, step=-2)
print(token[::-2])  # Effective start=len(token)-1, stop=-1, step=-2

#8.4
word = input("Enter a word: ").lower()
reversed_word = word[::-1]
print("Original word: {word}")
print("Reversed word: {reversed_word}")
if word == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")
print(f"First half of the word: {word[:len(word)//2]}")

#8.5
print("Enter your name: ")
name = input().strip()
cleaned_name = name.replace(" ", "")
print("Lowercase:", cleaned_name.lower())
print("Uppercase:", cleaned_name.upper())
print("Title Case:", cleaned_name.title())
print("First character (uppercase):", cleaned_name[0].upper())
print("Length before cleaning:", len(name))
print("Length after cleaning:", len(cleaned_name))
print("Contains only alphabetic characters:", cleaned_name.isalpha())

#8.6
email = input("Enter your email: ").strip().lower()
if "@" in email and "." in email:
    at_position = email.find("@")
    username = email[:at_position]
    ends_with_gmail = email.endswith("gmail.com")
    at_count = email.count("@")
print("Username:", username)
print("Position of '@':", at_position)
print("Ends with 'gmail.com':", ends_with_gmail)
print(f"Count of '@': {at_count}")

#8.7
File_name = input("Enter the file name: ").strip().lower()
if File_name.endswith((".pdf", ".docx", ".xlsx")):
    print("File is allowed for upload.")
    print("Contains 'report':", "report" in File_name)
    cleaned_file_name = File_name.replace(" ", "_")
    print("Cleaned file name:", cleaned_file_name)
    print("Last four characters:", cleaned_file_name[-4:])

#8.8
    Message = input("Enter a message: ")
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    Case_upper = 0
    Case_lower = 0
    Case_symbols = 0
    for char in Message:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
            if char.isupper():
                Case_upper += 1
            else:
                Case_lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            Case_symbols += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Uppercase letters:", Case_upper)
    print("Lowercase letters:", Case_lower)
    print("Symbols:", Case_symbols)

#8.9
incident_note = input("Enter the incident note: ").strip().lower()
if "error" in incident_note:
    error_count = incident_note.count("error")
    first_error_position = incident_note.find("error")
    updated_note = incident_note.replace("oldservice", "newservice")
    print(f"'error' exists: True")
    print(f"Count of 'error': {error_count}")
    print(f"Position of first 'error': {first_error_position}")
    print("Updated note:", updated_note)
#8.10
url = input("Enter the URL: ").strip()
if url.startswith("https://"):
    contains_login = "login" in url
    print("Contains 'login':", contains_login)
    ends_with_login_or_signin = url.endswith(("/login", "/signin"))
print("URL in lowercase:", url.lower())
print("Total length of URL:", len(url))

print("Ends with '/login' or '/signin':", ends_with_login_or_signin)

#8.11
username = input("Enter a username: ").strip().lower()
if len(username) < 5:
    print("Username must be at least 5 characters long.")
if username in ["admin", "root", "system"]:
    print("Username cannot be 'admin', 'root', or 'system'.")
if not username.isalnum():
    print("Username must contain only letters and digits.")
print("Username Accepted") if len(username) >= 5 and username not in ["admin", "root", "system"] and username.isalnum() else print("Username Rejected")

#8.12
password = input("Enter a password: ")
length_check = len(password) >= 8
uppercase_check = False
lowercase_check = False
digit_check = False
special_char_check = False

for char in password:
    if char.isupper():
        uppercase_check = True
    if char.islower():
        lowercase_check = True
    if char.isdigit():
        digit_check = True
    if char in "@#$!":
        special_char_check = True

if length_check and uppercase_check and lowercase_check and digit_check and special_char_check:
    print("Strong Password")
else:
    if not length_check:
        print("Password must be at least 8 characters long.")
    if not uppercase_check:
        print("Password must contain at least one uppercase letter.")
    if not lowercase_check:
        print("Password must contain at least one lowercase letter.")
    if not digit_check:
        print("Password must contain at least one digit.")
    if not special_char_check:
        print("Password must contain at least one of these special characters: @, #, $, !.")
    #8.13
    test_data = input("Enter the profile string (comma-separated): ")
    profile_parts = test_data.split(",")

    print("Name:", profile_parts[0])
    print("City:", profile_parts[1])
    print("Skill:", profile_parts[2])
    print("Level:", profile_parts[3])
    print("Total characters in profile string:", len(test_data))
    print("Contains 'Python':", "Python" in test_data)

#8.14
full_name = input("Enter your full name: ").strip().title()
if not full_name or full_name.isspace():
    print("Full name cannot be blank or only spaces.")
    full_name = None
username = input("Enter a username: ").strip().lower()
if len(username) < 5:
    print("Username must be at least 5 characters long.")
    username = None
if username in ["admin", "root", "system"]:
    print("Username cannot be 'admin', 'root', or 'system'.")
    username = None
email = input("Enter your email: ").strip().lower()
if "@" not in email or "." not in email:
    print("Email must contain '@' and '.'.")
    email = None
if email and not email.endswith("gmail.com"):
    print("Email must end with 'gmail.com'.")
    email = None
password = input("Enter a password: ")
if len(password) < 8:
    print("Password must be at least 8 character long.")
    password = None
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char in "@#$!" for char in password)

