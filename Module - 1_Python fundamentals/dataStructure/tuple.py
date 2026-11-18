# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "guava"
# fruits2 = ("apple", "banana", "cherry")
# # fruits2[0] = "mango"  -------------------> not allowed
# #
# # List -----> [ ]
# # tuple -----> ()
#
# print(fruits2[0])

numbers = (10,20,30,40,50)

print(numbers[1:4])
print(len(numbers))

# Tuple is immutable. Once created we cannot change, add or remove individual elements
# so these llist methods dont't work mon tuple :
#     append()
#     insert()
#     remove()
#     pop()
#     sort()