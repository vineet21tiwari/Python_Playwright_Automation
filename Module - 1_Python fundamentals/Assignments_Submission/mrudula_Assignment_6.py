#================1.Number Walk: 1 to 20===================
#1.  Use a for loop to print every number from 1 to 20, one number per line.
for i in range(1,21):
    print(i)
    #print(i, end=" ")
print("Loop completed")

#2.  Do not write twenty print statements.
#3.  After the loop, print Loop completed.

#================2.Reverse Countdown===============================
#1.  Print numbers from 15 down to 1 using a for loop.
for i in range(15,0,-1):
    print(i)
#2.  Use the third argument of range() instead of doing subtraction inside print().
#3.  After 1, print Go!


#===================3.Even Number Generator========================
#Generate values directly with range() rather than checking every number.
#1.  Print all even numbers from 2 to 40.
i=0
for i in range(2,41,2):
    if i%2==0:
        print("Even Number:", i)
#2.  Use a step value so only even numbers are generated.
#3.  Print the text Even: before each number