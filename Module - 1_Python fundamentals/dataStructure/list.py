# # without a a List
# student1 = "Rahul"
# student2 = "John"
# student3 = "murphy"
# #
# # List : it stores multiple values inside a single variable
# list = []
# for i in range(5):
#     x = int(input("Enter a number: "))
#     list.append(x)
#
# print(list)

# lets have  a list and findout  how many even and odd numbers are there
# numbers = [12,7,9,20,15,18]
# even_count = 0
# odd_count = 0
#
# for number in numbers:
#     if number % 2 == 0 :
#         even_count = even_count + 1
#     else :
#         odd_count = odd_count + 1
#
# print("Even: ", even_count)
# print("Odd: ", odd_count)

# Take a list of  student marks and find how many
# are passed and how many are failed , if passing marks is 40

#find maximum
# numbers = [10,23,2,14,39,24,12,1]
# # maximum= max(list)
# # minimum= min(list)
# maximum= numbers[0]
# minimum= numbers[0]
# for number in numbers:
#     if number > maximum:
#         maximum = number
#     if number < minimum:
#         minimum = number
#
# # max = 39
# # min = 1
# # number = 1
# print("Maximum: ", maximum)
# print("Minimum: ", minimum)

# Your program must:
# a. Take a sentence from the user and convert it into a word list using split().
# b. Print the word list and total number of words.
# c. Loop through the list and find the longest word manually.
# d. Count how many words have more than 5 characters.
# e. Sort the words alphabetically and print the final list.

sentence = input("Enter a sentence: ")

words = sentence.split()
print("word List ", words)

print("Total words ", len(words))

# longest_word = max(words)
longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word ", longest_word)

count = 0
for word in words:
    if len(word) > 5:
        count = count + 1

print("words with more than 5 characters ", count)
words.sort()
print("Sorted words ", words)

