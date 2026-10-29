age = int(input("Enter your age: "))
has_valid_id = input("Do you have a valid ID? (yes/no): ").strip().lower()
guardian_present = input("Is a guardian present? (yes/no): ").strip().lower()
allow_entry = (age >= 18 and has_valid_id == "yes") or (16 <= age <= 17 and guardian_present == "yes")
if allow_entry:
    print("Entry allowed.")
else:
    print("Entry denied.")
    additional_message = "You are too young to watch this movie" if age < 16 else ""
    print(additional_message)