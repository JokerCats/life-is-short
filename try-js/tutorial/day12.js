let arr = ['Apple', 'pear', 'orange'];

arr.forEach(x =>
    console.log(x)
);

// 标签函数：在模版字符串被解析前调用，对模版字符串进行处理（例如格式化/转译/国际化等）。
function tag(strings, ...values) {
    let result = '';
    strings.forEach(x => console.log("静态文言：" + x));
    values.forEach(x => console.log("插入文言：" + x));
    return result;
}

function tag2(strings, ...values) {
    let result = '';
    strings.forEach((string, i) => {
        console.log(`string ${string} i ${i}`);
    
        result += string + (values[i] || '');
    });
    return result.toUpperCase();
}

let name = 'Alice';
let address = "China"
let message = tag2`Hello ${name} from ${address}, welcome to the site!`;
console.log(message);