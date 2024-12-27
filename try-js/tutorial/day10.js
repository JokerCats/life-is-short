// 命名空间（名字空间）
// 避免所有的全局变量，方法绑定到 window 上

// 定义全局变量
let Student = {};

// 其他变量
Student.name = "zhangsan";
Student.age = 16;

// 其他函数
Student.eat = function() {
    console.log("student eating ..");
}

// let 声明块级作用域
// const 声明常量，同样具有块级作用域。另外常量通常大写。

// 解构数组变量时，应使用 [...] 括起来
// 从对象中抽取若干属性
let person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};

let {name, age, school} = person;
console.log(`school is ${school}`);
