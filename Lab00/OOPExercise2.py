class Student:
    def __init__(self, name, numberId, city):
        self.name = name
        self.numberId = numberId
        self.city = city

class School(Student):
    pass

school = School("Khoa Ho Tu Nhien", "12345678", "Ho Chi Minh City")
print(" Create a child class 'School' that will inherit all of the variables and methods of the 'Student' class")
print(school.name, school.numberId, school.city)