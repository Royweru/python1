from database import User

try:
    jina = input("Enter your name:\n")
    arafa = input("Enter email\n")
    siri = input("Enter password\n")

    User.create(name=jina, email=arafa, password=siri)

except:
    print('Failed to create user!!')

finally:
    print(f'user {jina} created successfully ')
