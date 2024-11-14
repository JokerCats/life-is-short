"""
求 1 ~ 100 的和
"""
total_a = 0
for x in range(101):
    total_a += x
print(f"1 ~ 100 的和：{total_a}")

"""
1~100 之间偶数求和
"""
total_b = 0
for x in range(2, 101, 2):
    total_b += x
print("偶数合计：%d" % total_b)

"""
猜数游戏
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入数字："))
    if number < answer:
        print("小于结果")
    elif number > answer:
        print("大于结果")
    else:
        print("等于结果")
        break
print(f'一共猜了{counter}次')

"""
乘法表
"""
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f'{y} * {x} = {x * y}', end='\t')
    print()

"""
判断用户输入是否为素数
素数：只能被 1 或自身整除且必须大于 1 的整数
"""
number = int(input("请输入一个整数："))
# 算法优化，减少循环次数
end = int(number ** 0.5)
# 检查范围内是否存在可以整除目标数字的数
is_prime = True
for x in range(2, end):
    if number % x == 0:
        is_prime = False
        break
if is_prime and number != 1:
    print("当前数字为素数 true")
else:
    print("当前数字为素数 false")