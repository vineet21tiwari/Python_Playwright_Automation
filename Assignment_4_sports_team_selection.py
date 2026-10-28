# A student can qualify for the sports team through performance in either speed or endurance, provided attendance
# is acceptable.
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# Take 100-metre race time, endurance score and attendance percentage.
# Qualify if race time is 14 seconds or less or endurance score is at least 80.
# Additionally, attendance must be at least 75.
# If sporting criteria pass but attendance fails, print Performance qualified - attendance insufficient.
# Otherwise print selected/not selected appropriately.
race_time = float(input("Enter 100-metre race time (in seconds): "))
endurance_score = int(input("Enter endurance score: "))
attendance_percentage = float(input("Enter attendance percentage: "))
attendance = attendance_percentage >= 75
if (race_time <= 14 or endurance_score >= 80) and attendance_percentage >= 75:
    print("Selected")
elif (race_time <= 14 or endurance_score >= 80) and attendance_percentage < 75:
    print("Performance qualified - attendance insufficient")
else:
    print("Not selected")