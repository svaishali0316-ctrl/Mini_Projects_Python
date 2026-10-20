# Student_Grade

name = input("Enter student name: ")

mark = float(input("Enter the student mark (0-100): "))

if mark ==100:
    print("Outstanding!")
elif mark >= 90:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C")
elif mark >= 60:
    print("Grade: D")
elif mark >= 50:
    print("Grade: E")
else:
    print("Grade: F")

print("Student name: ", name)
