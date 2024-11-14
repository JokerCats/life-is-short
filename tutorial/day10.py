class Student:
    # 限定类的属性
    # __slots__ = ("name", "age")

    def __init__(self, name, age):
        # 定义私有属性
        self.name = name
        # 定义成员属性
        self.age = age


stu = Student("Sam", 18)
print(stu.name, stu.age)

# 为 Student 类添加动态属性
stu.sex = "man"
print(f"新追加的属性（动态属性）：{stu.sex}")


# 定义父类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} 在吃饭。")

    def sleep(self):
        print(f"{self.name} 在睡觉。")


# 定义子类
class Student(Person):
    def study(self):
        print(f"{self.name} 正在学习 {self.age} 岁的知识。")

    # 子类复写父类方法
    def eat(self):
        print(f"{self.name} 现在什么也不想吃")


student = Student("Sam", 8)
student.eat()
student.study()
