from database import Student

try:
    jina = input('Input Your name: ')
    no = int(input('input your number: '))
    age = int(input('Input your age: '))
    gender = input('Input your gender: ')
    code = int(input('Enter your student code: '))
    Student.create(name=jina, phone=no, age=age, gender=gender, studentcode=code)
    print(f'student {jina} was registered successfully')
except:
    print('could not be able to register the student')
