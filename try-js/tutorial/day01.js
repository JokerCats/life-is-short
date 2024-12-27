// 启动 strict 模式
'use strict';

// 赋值语句
let x = 1;

// 不建议一行赋值多个语句
// var x = 1; var y = 2

/*
数据类型：
    Number
        123；整数
        0.456；浮点数
        1.234e2；科学计数法（123.4）
        -10；负数
        NaN；Not a Number（无法计算结果时）
        Infinity；无限大（超过 Number 能表示的范围）

    % 取余
字符串：
    '' or "" 包裹的内容
布尔值：
    true ｜ false
比较运算符：
    == 会自动类型转换，然后再比较。
    === 不会类型转换，由于设计缺陷请选择使用该比较方式。
    NaN 与自己比较依然为 false ， 通过 isNaN() 方法进行判断
BigInt：
    表示方法：在数字后加 n ｜ BigInt(123)
null：
    表示空值（大多数情况下使用该值）
undefined:
    表示未定义，仅在判断函数参数是否传递的情况下有用
 */

// 打印 Number 最大表示整数
console.log(Number.MAX_SAFE_INTEGER);

// 数组 [] | Array()
let array = [1, 2, 3, 4, 5];
// 出于代码可读性考虑，一般不使用这种方式进行声明
// var array2 = new Array(1, 2, 3);
console.log(array);

// 声明一个全局变量（仅在未启用 strict 模式下）
// i = 123

// \x 表示十六进制，\u 表示 Unicode