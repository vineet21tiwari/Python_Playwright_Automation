for number in range(1, 21):
    square = number ** 2
    if square > 150:
        print(f"The first number whose square is greater than 150 is: {number}")
        break