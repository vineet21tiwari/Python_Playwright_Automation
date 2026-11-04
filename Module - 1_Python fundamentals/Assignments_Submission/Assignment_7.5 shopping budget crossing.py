item_prices = list(range(100, 1001, 100))
total = 0

for price in item_prices:
    total += price
    if total > 2000:
        print(f"Current item price: {price}")
        print(f"Total: {total}")
        break