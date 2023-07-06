from peewee import *
from os import path

# creating our first database
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "emobilis.db"))


# creating table inside db
class User(Model):
    name = CharField(max_length=200)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


class Student(Model):
    name = CharField(max_length=200)
    phone = IntegerField()
    age = IntegerField()
    gender = CharField(max_length=20)
    studentcode = IntegerField()

    class Meta:
        database = db


User.create_table(fail_silently=True)
Student.create_table(fail_silently=True)
