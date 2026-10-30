# A library issues a book only when the member is active and does not have an overdue book.
# Take member-active status and overdue-book status.
# Issue the book if member is active and the user does not have an overdue book.
# If membership is inactive, print Renew membership first.
# If membership is active but overdue exists, print Return overdue book first.
# Use 
# not explicitly in at least one condition.
member_active = input("Is the member active? (yes/no): ").strip().lower() == "yes"
overdue_book = input("Does the member have an overdue book? (yes/no): ").strip().lower() == "yes"

if member_active and not overdue_book:
    print("Book issued successfully.")
elif not member_active:
    print("Renew membership first.")
else:
    print("Return overdue book first.")