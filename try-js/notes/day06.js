// Map 
// 定义：键值对，字典

// 声明对象
let student = new Map();

// 添加数据
student.set("Adam", 96);
student.set("Bob", 75);
student.set("City", 46);
console.log(student)

// 删除数据
student.delete("Bob");
console.log(student);

// 修改数据
student.set("City", 61);
console.log(student);

// 查询数据是否存在
console.log(`表中是否存在 Sam 的数据：${student.has("Sam")}`);

// 获取数据
console.log(student.get("Adam"));
