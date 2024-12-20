class Student:
    # 限定该类可定义的属性，仅对当前类有效，对子类无效。
    __slots__ = ("name", "age")


stu = Student()
stu2 = Student()

Student.name = "s1"
# Student.score = 99

print(stu.name)
print("-------------")
print(stu2.name)
print("-------------")
stu.score = 98
print(stu.score)
