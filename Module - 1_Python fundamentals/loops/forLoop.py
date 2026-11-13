# for i in range(5):
#     print(i)
#
# # print numbers from 1 to 20
# for i in range(1,21):
#     print(i, end = " ")

# print even numbers between 5 and 50
# for i in range(6,51,2):
#     print(i, end = " ")
#
# print("\n")
# for i in range(5,51):
#     if i % 2 == 0:
#         print(i, end = " ")


# print odd numbers from 12 to 60
# for i in range(13,60,2):
#     print(i, end = " ")

# take  a number from the user and write multiplication table for
# for example :
#     5 x 1 = 5
#     5 x 2 = 10
#     5 x 3 = 15
#     ..
#     ..
#     ..
#     5 x 10 = 50
# number = int(input("Enter a number: "))
# for i in range(1,11):
#     print(number, " x " , i, " = ", i*number)
#
# # print number from 10 to 80 which are divisible by 2 and 3
# for i in range(10,80,1):
#     if  i%2==0 and i%3==0:
#         print(i,end=' ')

# find how many numbers are there in between 18 to 180 which are divisible by 2 or 3 but not by 5
count = 0
for i in range(18, 181):
    if i%2 == 0 or i%3 == 0 and i%5 !=0 :
        count  =  count + 1

print("Total such numbers are : ", count)