import random

counters = [0] * 6

for _ in range(6000):
    face = random.randint(1, 6)
    # 记录随机次数
    counters[face - 1] += 1

for face in range(1, 7):
    print(f'{face} 出现了 {counters[face - 1]} 次')

# 最后一次出现的索引
s = 'hello good world!'
print(s.rfind('o'))

s2 = 'abc123456'
# 是否为数字
print(s2.isdigit())
# 是否为字母
print(s2.isalpha())
# 是否为数字和字母
print(s2.isalnum())

s3 = 'hello, world'
# 以宽度20将字符串居中并在两侧填充*
print(s3.center(20, '*'))  # ****hello, world****
# 以宽度20将字符串右对齐并在左侧填充空格
print(s3.rjust(20))  # hello, world
# 以宽度20将字符串左对齐并在右侧填充~
print(s3.ljust(20))  # hello, world~~~~~~~~
# 左侧补零
print('22'.zfill(5))

# 去除字符串两边的空格
string = ' jack@126.com 123'
print(string)
print(string.strip())

# 字符串的编码解码
a = '哈哈'.encode('utf-8')
b = a.decode('utf-8')
print(f'编码为：{a} 解码为：{b}')
