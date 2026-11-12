for employee_id in range(1001, 1021):
    if employee_id % 5 == 0:
        continue  # Skip reserved IDs
    print(f"Assigned ID: {employee_id}")    