from database import Student

students = Student.select()

for student in students:
    print(student.name, student.gender, student.age, student.phone, student.studentcode)
