
allowed_roles = ["admin", "manager", "tester"]
blocked_users = ["guest", "demo", "temp"]
username = input("Enter username: ").lower()
role = input("Enter role: ").lower()
balance = float(input("Enter account balance: "))
if role in allowed_roles and username not in blocked_users and balance >= 0:
    print("Access granted.")
if username in blocked_users:
    print("Blocked account.")
elif role not in allowed_roles:
    print("Unauthorized role.")
elif balance < 0:
    print("Insufficient funds.")
else:
    print("Access granted.")   