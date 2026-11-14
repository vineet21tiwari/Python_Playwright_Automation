from tkinter.messagebox import QUESTION

# QUESTION 1: PY-2026-VINEET
# Take the badge text from the user and print its total number of characters
# using len().
# Print the first character, last character, second character
# and second-last character using indexing.
# Print the first two characters as the course prefix using slicing.
# Print the last six characters using negative slicing.
# Print whether the first and last characters are the same

badge_txt1=input(print('please enter badge Text :'))
# wars should never happen not good for humanity
length_of_text = len(badge_txt1)
print(badge_txt1[:0])
print(badge_txt1[length_of_text-1])
print(badge_txt1[1])
print(badge_txt1[length_of_text-2])
course_first_word=badge_txt1[0:3]
print(course_first_word)
pre_fix=course_first_word[0:2]
print(pre_fix)
last_eight=badge_txt1[length_of_text-8:length_of_text]
print(last_eight)

# QUESTION 2:"HYD2026EXPRESS"
# # usingrint the first three characters a slice with an omitted start value.
# Print everything from index 3 to the end using an omitted stop value.
# Print the complete code using [:].
# Print characters from index 3 up to, but not including, index 7.
# For each slice above, write a comment
# identifying the effective start, stop and step

# wars should never happen not good for humanity
# usingrint the first three characters a slice with an omitted start value.
badge_txt2=input(print('please enter badge Text :'))
print(badge_txt2[:3])
# Print everything from index 3 to the end using an omitted stop value.
print(badge_txt2[3:length_of_text])
# Print the complete code using [:].
print(badge_txt2[:])
# Print characters from index 3 up to, but not including, index 7.
firstpart=badge_txt2[3:7]
print('broke the badge into two parts and then concat it to skip one letter')
print(firstpart)
secondpart=badge_txt2[8:]
print(secondpart)
print(firstpart+secondpart)
# we can use strip to do the same as below but could not achieve it
a=(badge_txt2[3:7])
b=badge_txt2.strip("E")
print(a)
print(badge_txt2)
print(b)

# QUESTION 3:
# A1B2C3D4E5F6
# Print every second character starting from the beginning using [::2].
# Print every second character starting from index 1 using [1::2].
# Print the token from index 2 to index 10 using a step of 2.
# Print the token in reverse using [::-1].
# Print the reversed token while taking every second character

Token= 'A1B2C3D4E5F6'
print(Token[::2])
print(Token[1::2])
print(Token[2:10:2])
print(Token[::-1])
reverced = Token[::-1]
print(reverced[::2])
# # QUESTION 4:
# Take a word from the user and normalize it to lowercase.
# Create a reversed version using slicing only.
# Print both the original normalized word and reversed word.
# Use if/else to print "Palindrome" when both are equal
# , otherwise print "Not Palindrome".
# Also print the first half of the word using slicing

user_word = input("Enter a word")
print(user_word[::-1])
if user_word.lower() == user_word[::-1].lower():
    print("Yes it is a Palindrome",user_word,user_word[::-1])
else:
    print("Not a Palindrome")
print(user_word[:int(len(user_word)/2):])

# QUESTION 5:
# vInEeT tiWaRi "
# Remove spaces from the beginning and end.
# Print the cleaned name in lowercase, uppercase and title case.
# Print only the first character of the cleaned name in uppercase.
# Print the length before cleaning and after cleaning.
# Check whether the cleaned name contains
# only alphabetic characters after removing the single space
# between first and last name using replace().

user_word = 'vInEeT tiWaRi'
print(user_word)
user_word1 = user_word.strip(" ")
print(user_word1)
print(user_word1)
print(user_word.lower())
print(user_word.upper())
print(user_word1.upper()[0:1:])
print(user_word1.isalpha())

# QUESTION 6:Remove outer spaces and convert the email to lowercase.
# Check that the email contains both "@" and "." using membership operators.
# Find the position of "@" using find().
# Use slicing to print the username portion before "@".
# Check whether the email ends with "gmail.com"
# and count how many times "@" appears

user_email=input(print('please enter a email address:'))
clean_email=user_email.lower().strip().replace(" ","")
print(clean_email)
if clean_email.__contains__("@") and clean_email.__contains__(".com"):
    print('it is a valid emailid position of @ is:',clean_email.find("@"))

user_id = clean_email[:clean_email.find("@")]
print(user_id)
# QUESTION 7:Take a file name and normalize it to lowercase.
# Accept the file only if it ends with .pdf, .docx or .xlsx.
# Print whether the name contains the word "report".
# Replace spaces in the file name with
# underscores and print the cleaned file name.
# Print the last four characters of the cleaned file name using slicing
file_name=input(print('Enter the file name to upload:'))
file_name1 = file_name.lower().strip(" ")
file_type=file_name[file_name.find("."):]
print(file_type)
if file_type == ".docx" or file_type == ".xlsx" or file_type == ".pdf":
    print('it is a valid file u can open it open file_name:')

else: print('it is not a valid file u should not open it:')
if file_name1.__contains__("report"):
        print(file_name1)
ln = len(file_name1) - 4
print(file_name1[ln:])
# # QUESTION 8:
# Loop through every character in the message.
# Count vowels and consonants separately.
# Count digits and spaces separately.
# Count uppercase and lowercase letters separately.
# Print all six counts with clear labels.
# Ignore symbols when counting consonants.

consonant_cnt=0
num_cnt=0
vowel_cnt=0
space_cnt=0
ascii_cnt=0
other_cnt=0
vowels =['a','e','i','o','u','A','E','I','O','U']
user_message=input('please enter a message:')
ln=len(user_message)
for i in user_message:
    if i.isalpha() and i not in vowels:
        consonant_cnt+= 1
    elif i.isalpha() and i in vowels:
        vowel_cnt+=1
    elif i.isnumeric():
        num_cnt+=1
    elif i.isspace():
       space_cnt+=1
    elif i.isascii():
        ascii_cnt+=1
else:other_cnt+=1
print(consonant_cnt)
print(vowel_cnt)
print(num_cnt)
print(space_cnt)
print(ascii_cnt)
print(other_cnt)

# QUESTION 09:Normalize the note to lowercase for case-insensitive checking.
# Check whether the word "error" exists.
# Count how many times "error" appears.
# Find the position of the first occurrence of "error".
# Replace every occurrence of "oldservice" with "newservice" and print the updated note

# QUESTION 10:Remove extra outer spaces from the URL.
# Check whether it starts with "https://".
# Check whether it contains the word "login".
# Check whether it ends with "/login" or "/signin".
# Print the URL in lowercase and print its total length.

user_url=input('please enter the URL to validate:')
user_url.strip()
if 'login' in user_url or user_url.endswith(['/login','/signin']):
    print('URL is a valid login page:',user_url.lower())
# QUESTION 11:Take a username, remove outer spaces and
# convert it to lowercase.
# Check that its length is at least 5 characters.
# Check that it is not one of these reserved values:
# admin, root, system.
# Use isalnum() to check whether it contains only letters and digits.
# Print a separate failure reason for every rule that the username violates;
# otherwise print "Username
# Accepted"

username = input("Enter your username: ")
username = username.strip().lower()
username_valid = False
if len(username) >= 5 and username not in ["admin", "root", "system"] and username.isalnum():
    username_valid = True
else:
    username_valid = False
if username_valid == True:
    print('username Accepted:')
else:
    print('username Rejected:')

# QUESTION 12:Take a password and verify that its length is at least 8.
# Loop through the password and detect whether at least one uppercase letter exists.
# Detect whether at least one lowercase letter and at least one digit exist.
# Detect whether at least one of these special characters exists: @, #, $, !.
# Print "Strong Password" only when every rule passes;
# otherwise print which requirements are missing
password = input("Enter your password: ")
has_uppercase = False
has_lowercase = False
has_digits = False
has_special = False

for i in password:
    if i.isupper():
        has_uppercase = True
    elif i.islower():
        has_lowercase = True
    elif i.isdigit():
        has_digits = True
    elif i in "@#$!":
        has_special = True

if (len(password) >= 8 and has_uppercase and has_lowercase
        and has_digits and has_special):
    password_valid = True
else:
    password_valid = False
if password_valid == False and len(password) < 8:
    print('password is not valid Length should be 8 or above:')
elif password_valid ==False and has_uppercase==False:
    print('password is not valid should have atleast one uppercase letter')
elif password_valid == False and has_lowercase==False:
    print('password is not valid should have atleast one lowercase letter')
elif password_valid ==False and has_digits==False:
    print('password is not valid should have atleast one digit')
elif password_valid == False and has_special==False:
    print('password is not valid should have atleast one special character')
else: print('password is  valid:')

# # QUESTION 14:Take the comma-separated profile string from the user.
# Use split(",") to separate the values.
# Print the first item as Name and the second item as City.
# Print the third item as Skill and the fourth item as Level.
# Print how many characters are present in the original profile string and whether the word "Python" exists in it


# QUESTION 14:Full name: strip outer spaces, convert to title case, and ensure it is not blank or only spaces.
# Username: lowercase it, require at least 5 characters, reject admin/root/system, and require letters/digits
# only.
# Email: lowercase it, require @ and ., print the username part before @, and check whether it ends with
# gmail.com.
# Password: require at least 8 characters and detect uppercase, lowercase, digit and one special character
# from @ # $ ! using a loop.
# Print a clear summary showing the normalized values and whether each field passed or failed


full_name = input("Enter your full name: ")
full_name = full_name.strip()

full_name = full_name.title()

if full_name != "":
    name_valid = True
else:
    name_valid = False


username = input("Enter your username: ")
username = username.strip().lower()

if len(username) >= 5 and username not in ["admin", "root", "system"] and username.isalnum():
    username_valid = True
else:
    name_valid = False

email = input("Enter your email address: ")
email = email.strip().lower()
if "@" in email and "." in email:
    email_valid = True

    at_positon = email.find("@")
    email_username = email[:at_positon]
else:
    email_valid = False
    email_username = "Not available"

if email.endswith("@gmail.com"):
    gmail_account = True
else:
    gmail_account = False

password = input("Enter your password: ")
has_uppercase = False
has_lowercase = False
has_digits = False
has_special = False

for i in password:
    if i.isupper():
        has_uppercase = True
    elif i.islower():
        has_lowercase = True
    elif i.isdigit():
        has_digits = True
    elif i in "@#$!":
        has_special = True

if len(password) >= 8 and has_uppercase and has_lowercase and has_digits and has_special:
    password_valid = True
else:
    password_valid = False