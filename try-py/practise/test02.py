def is_palindrome(n):
    str1 = str(n)
    str2 = str1[::-1]
    return str1 == str2


# 测试: 回文数（正着读反着读都一样的数）
output = filter(is_palindrome, range(1, 1000))
print("1~1000:", list(output))
if list(filter(is_palindrome, range(1, 200))) == [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    11,
    22,
    33,
    44,
    55,
    66,
    77,
    88,
    99,
    101,
    111,
    121,
    131,
    141,
    151,
    161,
    171,
    181,
    191,
]:
    print("测试成功!")
else:
    print("测试失败!")

# 按照名称进行排序
L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)


# 闭包练习
def createCounter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print("测试通过!")
else:
    print("测试失败!")


# 匿名函数改写
def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)


# 装饰器练习
import time, functools


def metric(fn):
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        print("%s executed in %s ms" % (fn.__name__, end_time - start_time))
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print("测试失败!")
elif s != 7986:
    print("测试失败!")
