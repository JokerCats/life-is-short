// 函数

// 定义关键字 function
function sum(a, b) {
    return a + b;
}

console.log(`a + b = ${sum(15, 23)}`);

// typeof 检查类型
// throw 抛出异常

// function 中有一个关键字 arguments，该关键字永远指向函数调用者传入的全部参数
function printStr() {
    for (let x = 0; x < arguments.length; x++) {
        console.log(`arguments is ${arguments[x]}`);
    }
}

printStr(10, 20, 30);

// rest 
// 参数：允许接收任意个参数
// 定义：...rest
function foo(a, b) {
    // 动态语言，所以声明时不必在意类型
    let rIndex, rest = [];
    let argumentSize = arguments.length
    if (argumentSize > 2) {
        for(rIndex = 2; rIndex < argumentSize; rIndex++) {
            rest.push(arguments[rIndex]);
        }
    }
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log('rest = ' + rest);
}

console.log('--------------');
foo();
console.log('-------');
foo(1);
console.log('-------');
foo(1, 2, 3, 4);
console.log('--------------');


function foo2(a, b, ...rest) {
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log('rest = ' + rest);
}

foo2();
console.log('-------');
foo2(1);
console.log('-------');
foo2(1, 3, 5, 7, 9);

// 由于 JS 会自动在行末添加分号，因此 return 语句的写法要变成下面这样
// return { - 防止自动加分号影响语义 ！！
//      xxx
// }
