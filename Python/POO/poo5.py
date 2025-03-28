from datetime import date
class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    @classmethod
    def calculate_age(cls,name,birth_year):
        #return new object
        return cls(name,date.today().year - birth_year)
    def show(self):
        print(self.name + "'s age is: " + str(self.age))
jessa = Student("Jessa",20)
jessa.show()
joy = Student.calculate_age("joy",1995)
joy.show()
