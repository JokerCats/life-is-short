// Set 
// 定义：一组 Key 的集合，不存储 Value 且 Key 不能重复。

// 声明对象
let student = new Set();

// 添加数据
student.add(1);
student.add(2);
student.add(2);
student.add(3);
console.log(student);

// 删除数据
student.delete(1);
console.log(student);