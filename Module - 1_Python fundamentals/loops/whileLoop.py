# import time
# count = 10
#
# while count >=1 :
#     print(count)
#     time.sleep(1)
#     count = count - 1
#
# print("Match started")

# find the sum of even numbers from 1 to 50
# 2 + 4 + 6 + ........... + 50 = ?
# num=50
# count=0
# while num%2==0:
#     print(num)
#     num=num-1
# count=count+1

# for the above code the ask is to calculate the sum

# i=2
# sum=0
# while i<=50:
#     if i%2==0:
#         sum = sum+i
#         # print('even number',i)
#     i=i+1
# print('sum of even numbers is', sum)

# keep taking the numbers until user enters 0 and print total
sum = 0
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    sum  =  sum + num
    num = int(input("Enter a number (0 to stop): "))

print("Total: ", sum)