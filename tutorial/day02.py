"""
身份验证
"""
name = input("please input your name: ")
code = input("please input your code: ")
if name == 'admin' and code == '1234':
    print("enter success.")
else:
    print("enter failure.")

"""
英寸和厘米转换
"""
value = float(input("请输入长度："))
unit = input("请输入单位：")
if unit == 'in' or unit == '英寸':
    print(f"{value:.2f}英寸 = {value * 2.54:.2f}厘米")
elif unit == 'cm' or unit == "厘米":
    print("%f厘米 = %f英寸" % (value, value / 2.54))
else:
    print("请输入有效单位")

"""
计算三角形的周长和面积
"""
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f"周长：{peri}")
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print("面积：%f" % area)
else:
    print("这不是一个三角形！")
