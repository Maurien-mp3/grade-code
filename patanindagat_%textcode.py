# Input from user
name = input("Enter your name: ")
section = input("What is your section? ")
preliminary = float(input("Enter your Preliminary grade (40-100): "))
midterm = float(input("Enter your Midterm grade (40-100): "))
final = float(input("Enter your Final grade (40-100): "))

# Check if grades are valid (between 40 and 100)
if (40 <= preliminary <= 100) and (40 <= midterm <= 100) and (40 <= final <= 100):
    
    # Calculate final grade as an average of the three grades
    calculated_grade = (preliminary + midterm + final) / 3
    calculated_grade = round(calculated_grade, 2)
    
    # Print the final grade
    print(f"\nYour final grade is: {calculated_grade}")

    # Determine and print the GPA based on the final grade
    if 99 <= calculated_grade <= 100:
        print("Your GPA is 1.00")
    elif 96 <= calculated_grade < 99:
        print("Your GPA is 1.25")
    elif 93 <= calculated_grade < 96:
        print("Your GPA is 1.50")
    elif 90 <= calculated_grade < 93:
        print("Your GPA is 1.75")
    elif 87 <= calculated_grade < 90:
        print("Your GPA is 2.00")
    elif 84 <= calculated_grade < 87:
        print("Your GPA is 2.25")
    elif 81 <= calculated_grade < 84:
        print("Your GPA is 2.50")
    elif 78 <= calculated_grade < 81:
        print("Your GPA is 2.75")
    elif 75 <= calculated_grade < 78:
        print("Your GPA is 3.00")
    else:
        print("Your GPA is 5.00 (Failing Grade)")
else:
    print("Invalid input! Grades should be between 40 and 100.")