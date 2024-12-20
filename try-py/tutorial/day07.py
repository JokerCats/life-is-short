"""
装饰器
定义：用一个函数装饰另外一个函数或类并为其提供额外功能
"""
import random
import time
from functools import wraps


def record_runtime(func):
    # 定义可以取消的装饰器函数
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} 执行时间：{end - start:.3f}秒')
        return result

    return wrapper


# 标记装饰器语法糖
@record_runtime
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


@record_runtime
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


# 使用装饰器语法糖
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器函数
download.__wrapped__("活着.word")

# func0 = record_runtime(download)
# func0('MySQL从删库到跑路.avi')
#
# func1 = record_runtime(upload)
# func1('Python从入门到住院.pdf')

# start = time.time()
# download('MySQL从删库到跑路.avi')
# end = time.time()
# print(f'花费时间: {end - start:.3f}秒')
# start = time.time()
# upload('Python从入门到住院.pdf')
# end = time.time()
# print(f'花费时间: {end - start:.3f}秒')
