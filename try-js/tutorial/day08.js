// Iterable
// 定义：集合类型，均可使用 for .. of 循环遍历
// 常见集合类型 [Array， Map， Set， String]
let str = "ABC";
for (let w of str) {
    console.log(w);
}

console.log("---------");

let array = [9, 8, 7, 6];
array.forEach(element => {
    console.log(`element : ${element}`);
});

console.log("---------");

array.forEach((element, index) => {
    console.log(`index : ${index} element : ${element}`);
});