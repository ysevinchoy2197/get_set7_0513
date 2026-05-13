#1-misol
class Student:
    def __init__(self, fullname, grade):
        self.fullname = fullname
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        self.__grade = new_grade


s1 = Student('Ali Valiyev', 4)

print(s1.fullname)
print(s1.get_grade())

s1.set_grade(5)
print(s1.get_grade())
