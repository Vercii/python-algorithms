class Student:
    def __init__(self,name,score,age):
        self.name = name
        self.score = score
        self.age = age
    def passed(self):
        if self.score >= 75:
            return "Passed"
        else:
            return "Failed"
    def display(self):
        print("Name:",student.name,"\nAge:",student.age,"\nScore:", student.score, "\nStatus:", self.passed(),"\n")

students = [
    Student("John", 70, 23),
    Student("Jane", 90, 21)
]

for student in students:
    student.display()

