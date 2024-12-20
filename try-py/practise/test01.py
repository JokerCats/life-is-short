# 列表生成式
print(list(range(1, 11)))
print(list(x * x for x in range(1, 11)))
print(list(x * x for x in range(1, 11) if x % 2 == 0))
print(list(x + y for x in "ABC" for y in "XYZ"))

import os

# 列出当前目录下所有文件
print(list(os.listdir(".")))

# 列表生成式前 if else 是表达式，后 if 是过滤条件，不能带 else
print(list(x if x % 2 == 1 else -x for x in range(1, 11)))

L1 = ["Hello", "World", 18, "Apple", None]
L2 = list(x.lower() for x in L1 if isinstance(x, str))

# 测试:
print(L2)
if L2 == ["hello", "world", "apple"]:
    print("测试通过!")
else:
    print("测试失败!")


def is_odd(num):
    return num % 2 == 1


def trim(str):
    return str and str.strip()


params = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
params2 = ["A", "", "B", None, "C", ""]

result = list(filter(is_odd, params))
print(result)

result2 = list(filter(trim, params2))
print(result2)


# 斐波那契数列
def fib(max):
    count = 0
    a, b = 0, 1
    while count < max:
        # print(f"a = {a} | b = {b}")
        yield b
        a, b = b, a + b
        count += 1
    return "done"


print(tuple(fib(6)))


# 杨辉三角形
def triangles():
    row = [1]
    while True:
        yield row
        row = [1] + [row[x] + row[x + 1] for x in range(len(row) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
]:
    print("测试通过!")
else:
    print("测试失败!")


# 获取 100 以内的素数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


# temp = _odd_iter()
# print(next(temp))
# print(temp.__next__())


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for x in primes():
    if x < 100:
        print(x)
    else:
        break
