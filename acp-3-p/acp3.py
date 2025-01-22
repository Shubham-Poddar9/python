age = int(input("Enter your age: "))
attendance = int(input("Enter your attendance percentage: "))

print(f"Your age: {age}")
print(f"Your attendance percentage: {attendance}%")

if age >= 14 and age <= 18:
    print("You meet the age criteria.")
    if attendance >= 75:
        print("You have enough attendance.")
        print("You are eligible for the exam.")
    else:
        print("Your attendance is less than 75%. You are not eligible for the exam.")
else:
    print("You do not meet the age criteria. You are not eligible for the exam.")
