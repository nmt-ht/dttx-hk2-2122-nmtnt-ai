class Student:
    def __init__(self, name, numberId, city):
        self.name = name
        self.numberId = numberId
        self.city = city

class School(Student):
    pass

school = School("Khoa Hoc Tu Nhien", "12345678", "Ho Chi Minh City")
print("Data - {school.name}: ", school.name)
print("Type of object: ", type(school))
student = Student("Nguyen Minh Tu", "21850024", "Ho Chi Minh City")
print("Data - {student.name}: ", student.name)
print("Type of object: ", type(student))