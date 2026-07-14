students = [
    {
        "name": "Alice",
        "score": 90
    },
    {
        "name": "Bob",
        "score": 60
    },
    {
        "name": "Charlie",
        "score": 88
    }
] # a list filled of dictionaries

# displays only passing students, making use of dictionaries
for student in students:
    if student["score"] >= 75:
        print(student["name"],"-",student["score"], "(Passed)")