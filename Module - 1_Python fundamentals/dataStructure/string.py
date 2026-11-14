# name = "PLAYWRIGHT"
#
# # Print characters from 3 to 7
# for i in range(3,8):
#     print(name[i], end="")

# Slicing
# Indexing gives one character
# Slicing gives multiple characters
#
# string[start:stop:step]
#
# start ---> Included
# end   ---> excluded


# name = input("Enter String: ")
# # for i in range(len(name)):
# #     print("Index  character")
# #     print(i, "         " +  name[i] )
#
# for i in name:
#     print(i)
#
# find how many 'a' character present in the given word
# word = "bananahjnhvjknjhnfljhirjfe"
# count = 0
# for i in word:
#     if i == 'a':
#         count += 1
# print(count)
# print(word.count('a'))



# In a given string find how many vowels and consonants are there
# word = input("Enter a word: ")
# word = word.lower()
#
# vowel = 0
# consonant = 0
#
# for i in word:
#     # if i in "aeiou":
#     #     vowel += 1
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         vowel += 1
#     elif i != " ":
#         consonant += 1
#
# print("vowel count : ", vowel)
# print("consonant count : ", consonant)

# print("hello " * 5)
# ------------------------------------------------------------------------------
#             STRING IMPORTANT METHODS
# -------------------------------------------------------------------------------
# name = "VINEET"
# name2  = "tiwari"
# fullname = name + " " + name2
# print(name.lower())
# print(name2.upper())
# print(fullname)
# print(fullname.title())  # it will capitalize begining of every word
# print(fullname.capitalize())  # it will capitalize only beginning of string


# username = "    admin     "
# print(username)
# print(username.strip())
#
# message = "I have fun doing Java"
# new_message = message.replace("Java","Python")
# print(new_message)

# find() : used to find particular substring
# message = "Python Playwright"
# print(message.find("Play"))
#
# word = "bananahjnhvjknjhnfljhirjfe"
# print(word.count('a'))
# print(word.find('a'))

# startsWith/ endsWith
# url = input("Enter URL: ")
# if url.startswith("https://"):
#     print("secure URL")
# else:
#     print("not secure")
#
#
# file_name = "reports.pdf"
# if file_name.endswith(".pdf"):
#     print("PDF file")
# else:
#     print("not a PDF file")

# isalpha() -------> true if only letters are there
# isalnum() -------> true if either letters or numbers are there
# isspace() -------> if SPACE

# name = "Vineet"
#
# print(name.isalpha())
# print("vineet123".isalpha())
# username = "Vineet123"
# print(username.isalnum())
#
# Q1 Take username from the user
#   remove unwanted outer spaces
#   convert to the lowercase
#   must be at least 5 characters
#   cannot be "admin" or "root"

# Q2 : Take password from the user
#         At least 8 characters
#         At least one uppercase
#         At least one lowercase
#         At least one digit
#         At least one special character

# q14

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
































