class Student:
    def __init__(self, name, numberId, city):
        self.name = name
        self.numberId = numberId
        self.city = city

studentModel = Student("Nguyen Minh Tu", "21850024", "Ho Chi Minh City")
print("Create a Class with instance attributes")
print(studentModel.numberId, studentModel.name, studentModel.city)