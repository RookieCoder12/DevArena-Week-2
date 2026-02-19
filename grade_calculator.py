name = str(input("Enter the name: "))

try:
    marks = int(input("Enter the number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

def grade_calculator(m : int):
    if m > 100:
        print("Invalid Score")
    else:
        if m in range(90, 101):
            print("Grade: A")
            print("Message: Excellent, keep up the good work.")
        elif m in range (80, 90):
            print("Grade: B")
            print("Message: Very Good, Keep it up.")
        elif m in range (70, 80):
            print("Grade: C")
            print("Message: Keep Going, You can improve.")
        elif m in range (60, 70):
            print("Grade: D")
            print("Message: Put in some work.")
        else:
            print("Grade: F")
            print("Message: You need to work a lot more harder.")

print(f"📊 Result for {name.capitalize()}: ")
print(f"Marks: {marks}")
grade_calculator(marks)