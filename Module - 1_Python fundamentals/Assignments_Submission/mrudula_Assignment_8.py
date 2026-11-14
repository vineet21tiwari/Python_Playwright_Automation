#1.==========================Student Badge Inspector================================
#A training portal stores a student badge text such as "PY-2026-VINEET". Build a small inspector that reports important parts of the badge.
#Your program must:
#a. Take the badge text from the user and print its total number of characters using len().
badge_num=input("Enter Badge number: ")
print("Badge Length:",len(badge_num))
#b.Print the first character, last character, second character and second-last character using indexing.
print("first character:",badge_num[0])
print("last character:",badge_num[-1])
print("second character:",badge_num[1])
print("second-last character:" ,badge_num[-2])
#c.Print the first two characters as the course prefix using slicing.
print("first two characters",badge_num[:2])
#d.Print the last six characters using negative slicing.
print("last six characters",badge_num[-6:])
#e.Print whether the first and last characters are the same
if badge_num[0] == badge_num[-1]:
    print("First and last characters are the same")
else:
    print("First and last characters are different")


#========================2.Delivery Tracking Code Slicer=========================
#A courier system receives a tracking code such as "HYD2026EXPRESS". The support team wants different parts of the same code without manually rewriting it.
#Your program must:
tracking_code=input("Enter tracking code: ")
#a.Print the first three characters using a slice with an omitted start value.
print("first three characters:",tracking_code[0:3])
#b.Print everything from index 3 to the end using an omitted stop value.
print("everything from index 3 to the end:",tracking_code[3:])
#c.Print the complete code using [:].
print("complete code:",tracking_code[:])
#d.Print characters from index 3 up to, but not including, index 7.
print("characters from index 3 up to, but not including, index 7:",tracking_code[3:-1:])
#e.For each slice above, write a comment identifying the effective start, stop and step


#=====================3.Security Token Sampler==========================
#A test environment produces a token string such as "A1B2C3D4E5F6". QA wants to sample characters at regular intervals.
#Your program must:
token_string="A1B2C3D4E5F6"
#a.Print every second character starting from the beginning using [::2].
print("every second character starting from the beginning:",token_string[::2])
#b.Print every second character starting from index 1 using [1::2].
print("every second character starting from index 1:",token_string[1::2])
#c.Print the token from index 2 to index 10 using a step of 2.
print("index 2 to index 10:",token_string[2:10:2])
#d.Print the token in reverse using [::-1].
print("token in reverse using:",token_string[::-1])
#e.Print the reversed token while taking every second character
print("reversed token while taking every second character:",token_string[::-2])


#=========================4.Mirror Word Challenge=============================
#A puzzle application needs to detect words that look the same from left to right and right to left.
#Your program must:
#a.Take a word from the user and normalize it to lowercase.
word=input("Enter word: ")
print(word.lower())
#b.Create a reversed version using slicing only.
print(word[::-1])
#c.Print both the original normalized word and reversed word.
print(word[::])
print(word[::-1])
#d.Use if/else to print "Palindrome" when both are equal, otherwise print "Not Palindrome".
if word==word[::-1]:
    print("word is Palindrome")
else:
    print("word is Not Palindrome")
#e.Also print the first half of the word using slicing
print(word[:len(word)//2])

#=======================5.Customer Name Cleaner========================
#A registration form often receives names with extra spaces and inconsistent capitalization, for example "vInEeT tiWaRi ".
#Your program must:
name="vInEeT tiWaRi "
#a.Remove spaces from the beginning and end.
print(name.strip())
#b.Print the cleaned name in lowercase, uppercase and title case.
print(name.strip().lower())
print(name.strip().upper())
print(name.strip().title())
# c.Print only the first character of the cleaned name in uppercase.
print(name[0].upper())
# d.Print the length before cleaning and after cleaning.
print(len(name))
clean_name=name.strip()
print(len(clean_name))
# e.Check whether the cleaned name contains only alphabetic characters after removing the single space between first and last name using replace().
new_name=clean_name.replace(" ","")
print(new_name)
if new_name.isalpha():
    print("Clean name contains only alphabetic")
else:
    print("Clean name does not contain only alphabetic")



#========================6.Email Address Analyzer================================
#A test script needs to quickly inspect an email entered by a user.
#Your program must:
email=input("Enter email: ")
# a.Remove outer spaces and convert the email to lowercase.
print("Remove outer spaces:",email.strip())
print("Email in lowercase:",email.strip().lower())
# b.Check that the email contains both "@" and "." using membership operators.
if email in "@" and email in ".":
# c.Find the position of "@" using find().
    print(email.find("@"))
# d.Use slicing to print the username portion before "@".
print(email[:email.index("@")])
# e. Check whether the email ends with "gmail.com"
if email.endswith("gmail.com"):
    print("Email ends with gmail.com")
else:
    print("Email does not end with gmail.com")

# Count how many times @ appears
print(email.count("@"))