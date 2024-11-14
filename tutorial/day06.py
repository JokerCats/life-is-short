"""
命名关键字参数
强制用户使用命名参数时，可在参数列表前追加 * 号
* 号前的参数是位置参数，* 号后的参数是关键字参数
"""


def is_triangle(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b


"""
位置参数必须在关键字参数之前，否则会引发异常

可变参数 *args （元组）
可变关键字参数 **kwargs （字典）

万物皆对象，函数也可以作为一个对象。
将函数作为函数的参数即为高阶函数。
高阶函数的目的在于解耦，提高函数的灵活性。
"""

import operator


def calc(*args, op):
    result = 0
    for arg in args:
        result = op(result, arg)
    return result


print(calc(1, 2, 3, op=operator.add))

"""
Lambda 表达式 （匿名函数）
格式： lambda 参数: 表达式
解析： 关键字  参数: 返回值
在 Python 中若一行代码能实现的情况下，尽量使用 Lambda 表达式来书写。
"""
