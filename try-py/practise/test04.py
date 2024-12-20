import sys

print(sys.path)


# object 是所有类的父类
class Student(object):
    # 类方法的第一个参数始终是 self，其余和普通方法无异
    # __init__ 用于定义实例化方法
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_scpre(self):
        print(f"{self.__name}:{self.score}")

    def set_name(self, new_name):
        self.__name = new_name


if __name__ == "__main__":
    stu = Student("A", 86)
    stu.print_scpre()
    # 这里修改的 name 字段是一个新的字段，并不是 stu 的
    # stu 内部的 name 字段已变成 _Student__name
    # 因此下面的代码相当于新创建了一个字段。
    stu.__name = "B"
    print(stu.__name)

    stu.print_scpre()

    stu.set_name("C")
    print(stu.__name)

    stu.print_scpre()


## 练习
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student("Bart", "male")
if bart.get_gender() != "male":
    print("测试失败!")
else:
    bart.set_gender("female")
    if bart.get_gender() != "female":
        print("测试失败!")
    else:
        print("测试成功!")
