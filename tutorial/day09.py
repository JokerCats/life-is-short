class Student:

    def __init__(self, name, age):
        # 定义私有属性
        self.__name = name
        # 定义成员属性
        self._age = age

    # 属性访问器
    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self._age

    # 属性修改器
    @name.setter
    def name(self, name):
        # 三元运算写法
        # self.__name = name if name else "unknown"
        self.__name = name or "unknown"


stu = Student("Sam", 18)
print(stu.name, stu.age)

stu.name = ""
print(stu.name)

stu.name = "Trump"
print(stu.name)
