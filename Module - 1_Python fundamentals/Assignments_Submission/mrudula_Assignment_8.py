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


#===================================7.File Upload Gatekeeper=================================
#An automation test must validate whether a selected file is an allowed document before upload.
#Your program must:
#a.Take a file name and normalize it to lowercase.
file_name=input("Enter file name: ")
normalize_name=file_name.strip().lower()
print(normalize_name)
#b.Accept the file only if it ends with .pdf, .docx or .xlsx.
if normalize_name.endswith((".mp4",".pdf",".docx",".xlsx")):
    print("Filename Accepted")
else:
    print("Filename Rejected")
#c.Print whether the name contains the word "report".
if "report" in normalize_name:
    print("Filename has a word called report")
else:
    print("Filename has NO word called report")
#d.Replace spaces in the file name with underscores and print the cleaned file
clean_file= normalize_name.replace("","_")
print("Filename Replaced with Underscore",clean_file)
# e.Print the last four characters of the cleaned file name using slicing
print(normalize_name[-4:])






#==============================8.Support Message Character Report==================================
#A support chatbot receives a message and the QA team wants a character-level report.
# #Your program must:
# a.Loop through every character in the message.
message="This is Mrudula Mutyala Learning Playwright with Python"
vowel_count=0
cons_count=0
digit_count=0
space_count=0
uppercase_count=0
lowercase_count=0
for i in message:
    print(i,end=" ")
# b.Count vowels and consonants separately.
    if i.isalpha():
        if i.lower() in "aeiou":
            vowel_count+=1
        else:
            cons_count+=1
# c.Count digits and spaces separately.
    if i.isdigit():
        digit_count+=1
    if i.isspace():
        space_count+=1
# d.Count uppercase and lowercase letters separately.
    if i.isupper():
        uppercase_count+=1
    if i.islower():
        lowercase_count+=1

# e.Print all six counts with clear labels. Ignore symbols when counting consonants
print("Vowel Count:",vowel_count)
print("Consonant count",cons_count)
print("Digit Count",digit_count)
print("Space Count:",space_count)
print("Uppercase Count:",uppercase_count)
print("Lowercase Count",lowercase_count)




#=========================9.Incident Keyword Scanner============================================================
#An incident note may contain repeated words such as "error" and an old service name that needs to be replaced.
#Your program must:
#a.Normalize the note to lowercase for case-insensitive checking.
note="This is note that contains error multiple time error Error ERROR ErrOR with oldservice"
normalize_note=note.strip().lower()
print(normalize_note)
# b.Check whether the word "error" exists.
if "error" in normalize_note:
    print("Note contains a word called Error")
else:
    print("Note does not contains a word called Error")
# c.Count how many times "error" appears.
print(normalize_note.count("error"))
# d.Find the position of the first occurrence of "error".
print(normalize_note.find("error"))
# e.Replace every occurrence of "oldservice" with "newservice" and print the updated note.
print(normalize_note.replace("oldservice","newservice"))


#============================10.Secure URL Checker====================================================
#A browser automation suite receives URLs from test data and should reject obviously invalid endpoints.
#Your program must:
# a.Remove extra outer spaces from the URL.
url="    http://C:/Users/hello/PycharmProjects/Python_Playwright_Automation/Module%20-%201_Python%20fundamentals/Assignments/login    "
clean_url=url.strip()
print(clean_url)
# b.Check whether it starts with "https://".
if clean_url.startswith("http"):
    print("URL starts with http")
else:
    print("URL does not start with http")
# c.Check whether it contains the word "login".
if "login" in clean_url:
    print("URL contains login")
else:
    print("URL does not contain login")
# d.Check whether it ends with "/login" or "/signin".
if clean_url.endswith("/login") or clean_url.endswith("/signin"):
    print("URL ends with login/signin")
else:
    print("URL does not ends with login/signin")
# e.Print the URL in lowercase and print its total length
lowercase_url=clean_url.lower()
print(lowercase_url)
print(len(lowercase_url))


#==============================11.Username Quality Check===================================
#A website requires usernames that are easy to store and validate.
# Your program must:
# a.Take a username, remove outer spaces and convert it to lowercase.
username="               MrudulaMutyala_system2026              "
clean_username=username.strip()
print(clean_username)
print(clean_username.lower())
# b.Check that its length is at least 5 characters.
if len(clean_username)>=5:
    print("Username contains atleast 5 characters:",len(clean_username))
else:
    print("Username does not contain atleast 5 characters:",len(clean_username))
# c.Check that it is not one of these reserved values: admin, root, system.
if "admin" in clean_username or "root" in clean_username or "system"  in clean_username:
    print("Username does contains values: admin, root, system.")
else:
    print("Username does not contains values: admin, root, system.")
# d.Use isalnum() to check whether it contains only letters and digits.
if clean_username.isalnum():
    print("Username does contains alphanum characters:",clean_username)
else:
    print("Username does not contain alphanum characters:",len(clean_username))
# e.Print a separate failure reason for every rule that the username violates; otherwise print "Username Accepted"
if len(clean_username)>=5 and "admin" not in clean_username and "root" not in clean_username and "system" not in clean_username and clean_username.isalnum():
    print("Username Accepted",clean_username)
else:
    print("Username Rejected",clean_username)





#==========================12.Password Strength Inspector======================Need to WORK
#A registration screen needs a basic password-strength check. Do not use regular expressions.
# Your program must:
# a.Take a password and verify that its length is at least 8.
password="TestPython123@"
uppercase_found=False
lowercase_found= False
digit_found=False
special_found=False
if len(password)>=8:
    print("Password is longer than 8 characters:",len(password))
else:
    print("Password is shorter than 8 characters:",len(password))
# b.Loop through the password and detect whether at least one uppercase letter exists.
for char in password:
    if char.isupper():
        uppercase_found= True
# c.Detect whether at least one lowercase letter and at least one digit exist.
    if char.islower():
        lowercase_found= True

    if char.isdigit():
        digit_found= True
# d.Detect whether at least one of these special characters exists: @, #, $, !.
    if char in ("@","#","$","!"):
        special_found= True
# e.Print "Strong Password" only when every rule passes; otherwise print which requirements are missing
if uppercase_found==True and lowercase_found==True and digit_found==True and special_found==True:
    print("Strong Password")
else:
    print("requirements are missing")




#================================13.CSV Profile Reader==============================
#A small test-data line arrives as "Vineet,Hyderabad,Python,Senior". You need to break it into meaningful values.
#Your program must:
# a.Take the comma-separated profile string from the user.
profile_string = "Mrudula,Hopkinton,Python,Experienced"
# b.Use split(",") to separate the values.
profile= profile_string.split(",")
# c.Print the first item as Name and the second item as City.
print("name:",profile[0])
print("City:",profile[1])
# d.Print the third item as Skill and the fourth item as Level.
print("Skill:",profile[2])
print("Level:",profile[3])
# e.Print how many characters are present in the original profile string and whether the word "Python" exists in it
print("Length of original profile string:",len(profile_string))
print("Length of original profile string:",len(profile))
if "Python" in profile:
    print("Python exists in Profile String")
else:
    print("Python not in Profile String")







#===================================14.Final Registration Text Validator===============================
#Build a single console program for a registration screen. It should validate full name, username, email and password using the string concepts from this assignment.
#Your program must:
# a.Full name: strip outer spaces, convert to title case, and ensure it is not blank or only spaces.
full_name= "                       mrudula Mutyala                         "
clean_name= full_name.strip().title()
print("Full name:",clean_name)
if clean_name== "":
    print("fullName cant be blank:",clean_name)
else:
    print("fullName is:",clean_name)
# b.Username: lowercase it, require at least 5 characters, reject admin/root/system, and require letters/digits only.
username="MrudulaMutyala_system2026"
print("Username:",username.lower())
if len(username)>=5:
    print("Username contains atleast 5 characters:",len(username))
else:
    print("Username does not contain atleast 5 characters:",len(username))
if "admin" in username or "root" in username or "system" in username:
    print("Username should NOT contains values: admin, root, system.")
else:
    print("Username:",username)
if username.isalnum():
    print("Username Contain alphanum characters:",username)
else:
    print("Username does not contain alphanum characters:",username)
# c.Email: lowercase it, require @ and ., print the username part before @, and check whether it ends with gmail.com.
email="Mrudula.Mutyala@gmail.com"
print("Email:",email.lower())
if "@" in email and "." in email:
    print("Email address contain dot  and @ characters:",email)
else:
    print("Email address does not contain dot and  @ characters:",email)
email_position=email.find("@")
print("Email Username",email[:email_position])
if email.endswith("gmail.com"):
    print("Email address ends with gmail.com",email)
else:
    print("Email address does not end with gmail.com")
# d.Password: require at least 8 characters and detect uppercase, lowercase, digit and one special character from @ # $ ! using a loop.
password="Password0987!^"
uppercase_found=False
lowercase_found=False
digit_found=False
special_found=False
if len(password)>=8:
    print("Password is longer than 8 characters:",len(password))
for char in password:
    if char.isupper():
        uppercase_found= True
    if char.islower():
        lowercase_found= True
    if char.isdigit():
        digit_found= True
    if char in ("@","#","$","!"):
        special_found= True
# e.Print a clear summary showing the normalized values and whether each field passed or failed
if uppercase_found==True and lowercase_found==True and digit_found==True and special_found==True:
    print("Password Requirement Passed")
else:
    print("Password Requirement Rejected")