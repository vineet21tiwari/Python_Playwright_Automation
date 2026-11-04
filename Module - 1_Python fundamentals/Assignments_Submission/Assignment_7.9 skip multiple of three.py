count = 0
for number in range(1, 51):
    if number % 3 == 0:
        continue
    count += 1
    print(number)
print(f"Total numbers processed: {count}")  