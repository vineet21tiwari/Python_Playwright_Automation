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

# find how many 'a' character present in the given word
# word = "bananahjnhvjknjhnfljhirjfe"
# count = 0
# for i in word:
#     if i == 'a':
#         count += 1
# print(count)

# In a given string find how many vowels and consonants are there
word = input("Enter a word: ")
word = word.lower()

vowel = 0
consonant = 0

for i in word:
    # if i in "aeiou":
    #     vowel += 1
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel += 1
    elif i != " ":
        consonant += 1

print("vowel count : ", vowel)
print("consonant count : ", consonant)
