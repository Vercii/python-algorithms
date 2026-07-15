class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class Student(Person):
    pass

student = Student("Renzo",23)
print(student.name,student.age)