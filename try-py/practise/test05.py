class Animal:
    def eat():
        print("animal is eating.")


class Dog(Animal):
    def run():
        print("dog is running.")


a = Animal()
d = Dog()

# 使用 isinstance 判断是否是某个类型
print(isinstance(a, Dog))
print(isinstance(d, Dog))
# 使用 issubclass 判断是否是某个类型子类
print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))

# 获取对象所有的属性和方法 dir
print(f"String 的属性和方法：{dir("")}")
# 为对象设置属性值 x
setattr(object, "x", 1)
# 获取对象的 x 属性或方法，如果没获取到则返回默认值 404
getattr(object, "x", 404)
# 检查对象是否存在 x 属性
hasattr(object, "x")


class Student:
    # 类属性
    name = "HaHa"


stu = Student()
print(stu.name)

stu.name = "Bob"
print(stu.name)

Student.name = "City"

del stu.name
print(stu.name)
