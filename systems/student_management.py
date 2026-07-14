student_count = int(input("Enter number of students: "))
students = []

for _ in range(student_count):
    name = input(f"Enter the name for student {_ + 1}: ")
    score = int(input(f"Enter the score for student {_ + 1}: "))

    students.append({
        "name": name,
        "score": score, 
    })

for student in students:
    if student["score"] >= 75:
        print(student["name"],"-",student["score"], "(Passed)")