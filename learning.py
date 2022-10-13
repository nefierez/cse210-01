"""
class Student:
    pass

student_1 = Student()
student_2 = Student()
student_3 = Student()
student_4 = Student()
student_5 = Student()

student_1.first = 'Greis'
student_1.last = 'Garcia'
student_1.email = 'greisgarcia01@gmail.com'
student_1.age = 20

student_2.first = 'Ron'
student_2.last = 'Robanjin'
student_2.email = 'ron.robanjin02@gmail.com'
student_2.age = 25

student_3.first = 'Sariah'
student_3.last = 'Tanner'
student_3.email = 'sariahtanner03@gmail.com'
student_3.age = 30

student_4.first = 'Robin'
student_4.last = 'Dickson'
student_4.email = 'robindickson04@gmail.com'
student_4.age = 30

student_5.first = 'Nefi'
student_5.last = 'Perez'
student_5.email = 'nefiperez2018@gmail.com'
student_5.age = 25

print(student_1.first + ' email address is ' + student_1.email)
print(student_2.first + ' email address is ' + student_2.email)
print(student_3.first + ' email address is ' + student_3.email)
print(student_4.first + ' email address is ' + student_4.email)
print(student_5.first + ' email address is ' + student_5.email)


"""
class Student:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + '.' + last + "@byui.edu"

student_1 = Student('Greis', 'Garcia', 20)
student_2 = Student('Ron', 'Robanjin', 25)
student_3 = Student('Sariah', 'Tanner', 30)
student_4 = Student('Robin', 'Dickson', 30)
student_5 = Student('Nefi', 'Perez', 25)

print(student_1.first + ' email address is ' + student_1.email)
print(student_2.first + ' email address is ' + student_2.email)
print(student_3.first + ' email address is ' + student_3.email)
print(student_4.first + ' email address is ' + student_4.email)
print(student_5.first + ' email address is ' + student_5.email)