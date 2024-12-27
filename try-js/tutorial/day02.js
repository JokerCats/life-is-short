// 多行字符串
let string = `
    hello
    world
`;
console.log(string);

// 字符串连接
let userName = 'zhangsan';
let age = 20;
let message = '1. hello ' + userName + ' your age is ' + age;
console.log(message);
// 模版字符串
let message2 = `2. hello ${userName} your age is ${age}`;
console.log(message2);
// 获取字符串长度
console.log(message.length);

// 字符串是不可变的，因此修改无效
let s = "123";
s[0] = '5';
console.log(s);

let str = 'hello world';
// 将字符串变为大写
console.log(str.toUpperCase());
// 将字符串变为小写
console.log(str.toLowerCase());
// 查找字符位置
console.log(str.indexOf('o'));
// 获取指定索引区间的字符
console.log(str.substring(0, 3))