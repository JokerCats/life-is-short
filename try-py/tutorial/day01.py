"""
将华氏温度转换为摄氏温度
"""
f = float(input("请输入华氏温度： "))
c = (f - 32) / 1.8
print("%.1f华氏温度 = %.1f摄氏温度" % (f, c))
print(f"{f:.1f}华氏温度 = {c:.2f}摄氏温度")

"""
根据半径计算周长和面积
"""
PI = 3.141592653589793
radius = float(input("请输入圆的半径："))
perimeter = 2 * PI * radius
area = PI * radius ** 2
print("周长：%.2f" % perimeter)
print(f"面积：{area:.2f}")

"""
判断用户输入年份是否是闰年
"""
year = int(input("请输入要查询的年份："))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"当前年份是闰年：{is_leap}")

