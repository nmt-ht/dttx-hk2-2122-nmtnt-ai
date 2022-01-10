class Student:
    def __init__(self, name, numberId, city):
        self.name = name
        self.numberId = numberId
        self.city = city
    def set_yearsold(self, years_old):
        return f"The years old of {self.name} is {years_old}"

class School(Student):
    def set_yearsold(self, years_old=100):
        return super().set_yearsold(years_old)

school_yearsOld = School("Khoa Hoc Tu Nhien", "12345678", "Ho Chi Minh City")
print("Class Inheritance")
print(school_yearsOld.name, school_yearsOld.numberId, school_yearsOld.city)
print(school_yearsOld.set_yearsold())