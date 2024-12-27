// 数组中可以包含类型不同的数据
let arr = ['A', 'B', 'C'];
console.log(arr.length);

// 调整数组大小
arr.length = 5;
console.log(arr);
arr.length = 2;
console.log(arr);

// 添加的索引数据超出范围会导致数据大小自动扩大
arr[5] = 'D';
console.log(arr);

// 对应 String 的 subString 方法
let arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
console.log(arr);
console.log(arr.slice(1, 3));
console.log(arr.slice(3));

// 向数组追加元素
arr.push(1, 2);
console.log(arr);
// 从数组中移除末尾元素
arr.pop();
console.log(arr);

// 向数组头部添加数据
arr.unshift("first");
console.log(arr);
// 移除头部数据
arr.shift();
console.log(arr);

// sort 排序
// reverse 反转

let arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
// 追加数据
arr.splice(2, 0, "Google");
console.log(arr);
// 删除数据
arr.splice(0, 1);
console.log(arr);
// 删除并追加数据
arr.splice(4, 2, "Facebook");
console.log(arr);

// 拼接数组
let arr2 = ['A', 'B'];
console.log(arr.concat(arr2));

// 使用指定字符串联
let arr3 = ['小明', '小红', '大军', '阿黄'];
console.log(arr3.join('-'));