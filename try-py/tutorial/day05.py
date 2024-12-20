"""
计算参数合计
"""


def jk_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


"""
生成验证码
"""
import random
import string

print(string.digits)
print(string.ascii_letters)


def generate_code(code_len=4):
    ALL_CHARS = string.digits + string.ascii_letters
    return ''.join(random.choices(ALL_CHARS, k=code_len))


print(f'code is {generate_code(6)}')

"""
获取文件名称
默认参数，三元运算的写法
"""


def get_suffix(filename='', ignore=False):
    dot_index = filename.rfind('.')
    if dot_index <= 0:
        return ''
    return filename[dot_index + 1:] if ignore else filename[dot_index:]


from os.path import splitext

"""
使用系统的方式获取扩展名
"""


def get_suffix2(filename, ignore=True):
    return splitext(filename)[1][1:] if ignore else splitext(filename)[1]


print(get_suffix('readme.txt'))  # txt
print(get_suffix('readme.txt.md'))  # md
print(get_suffix('.readme'))  #
print(get_suffix2('readme.'))  #
print(get_suffix('readme'))  #

"""
判断自然数是否为质数
"""


def is_prime(num):
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return num != 1


print(f'7 是质数：{is_prime(7)}')
print(f'4 是质数：{is_prime(4)}')
