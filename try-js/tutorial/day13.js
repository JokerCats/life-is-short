// 生成器函数
function* foo(x) {

}

// 不要使用new Number()、new Boolean()、new String()创建包装对象；
// 用parseInt()或parseFloat()来转换任意类型到number；
// 用String()来转换任意类型到string，或者直接调用某个对象的toString()方法；
// 通常不必把任意类型转换为boolean再判断，因为可以直接写if (myVar) {...}；
// typeof操作符可以判断出number、boolean、string、function和undefined；
// 判断Array要使用Array.isArray(arr)；
// 判断null请使用myVar === null；
// 判断某个全局变量是否存在用typeof window.myVar === 'undefined'；
// 函数内部判断某个变量是否存在用typeof myVar === 'undefined'。

// JSON 
// 序列化：stringify
// 反序列化：parse
let json = {
    "name": "Alice",
    "age": 18
};
console.log("-----------------");

console.log(`json => ${JSON.stringify(json)}`);
console.log("-----------------");

// 美化输出
console.log(`json 2 => ${JSON.stringify(json, null, '    ')}`);
console.log("-----------------");

// 仅输出筛选后的对象
console.log(`json 3 => ${JSON.stringify(json, ['age'], '    ')}`);

// 解析的同时追加处理
let parse = JSON.parse(
    JSON.stringify(json),
    function (key, value) {
        if (key === "name") {
            return value + "同学";
        }
        return value;
    }
);
console.log("-----------------");
console.log(`json 4 => ${parse['name']}`);
