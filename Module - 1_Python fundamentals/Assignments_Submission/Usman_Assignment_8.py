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
# Print all six counts with clear labels. Ignore symbols when counting consonants.