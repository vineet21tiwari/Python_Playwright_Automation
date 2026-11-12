# A passenger is looking for one specific seat in a bus.
# 1. Loop through seat numbers 1 to 40 using range().
# 2. The requested seat number is 23. When seat 23 is reached, print Requested seat found and stop the
# loop.
# 3. After the loop, print Search finished
for seat in range(1,41):
    if seat == 23:
        print("Requested seat found")
        break
else:
        print("Requested seat not found")
print("search finsihed")