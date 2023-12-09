# 09.12.23. Sergii Logosha sergiilogosha@gmail.com

class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa


nora = Student('245AFS', 'Nora', 15, 3.97)

print(nora._age)
