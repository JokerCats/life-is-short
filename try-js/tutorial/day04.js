// 使用 {} 表示对象
let student = {
    userName: 'ABC',
    age: 19
};
console.log(student.userName);

// 删除对象中的属性
delete student.userName;
// 查询不存在的属性，将返回 undefined
console.log(student.userName);

// 检查对象是否存在某个属性
console.log(`对象存在 age 属性：${'age' in student}`);
console.log(`对象存在 userName 属性：${'userName' in student}`);

// 通过 in 判断的结果可能包含父类
// student 继承自 object，object 类中存在 toString 方法
console.log(`对象存在 toString 方法：${"toString" in student}`);
// 仅检查当前类是否存在
console.log(`hasOwnProperty age : ${student.hasOwnProperty('age')}`);
console.log(`hasOwnProperty toString : ${student.hasOwnProperty('toString')}`);