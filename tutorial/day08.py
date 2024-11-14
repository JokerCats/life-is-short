class Student:
    def __init__(self, name, age):
        # 定义私有属性
        self.__name = name
        # 定义成员属性
        self._age = age

    def study(self, course_name):
        print(f"{self.__name} learning {course_name}.")

    def play(self):
        print(f"{self.__name} plays games for ages {self._age} and up.")


stud1 = Student("StudentA", "22")
stud2 = Student("StudentB", "8")

stud1.study("English")
stud2.play()

print(stud1._age)
# 强行访问私有属性
print(stud2._Student__name)
