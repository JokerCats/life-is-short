'use strict';

let xiaoming = {
    name: '小明',
    birth: 2000,
    age: function () {
        let y = new Date().getFullYear();
        return y - this.birth;
    }
};

console.log(xiaoming.age());

// apply 用来改变 this 指向，它的第一个参数就表示改变后的 this 指向
// call 与 apply 的作用是一样的，区别在于传入参数的方式不同

function sum(a, b) {
    return a + b;
}
console.log([1].reduce(sum));

function str2int(s) {
    let array = s.split('').map(
        function (x) {
            return x - '0';
        }
    );
    return array.reduce(
        function (x, y) {
            return x * 10 + y;
        }
    );
}
console.log(str2int('123'));


function get_primes(arr) {
    let arr2 = arr.filter(function (x) {
        if (x < 2) {
            return false;
        }
        for (let i = 2; i < x; i++) {
            if (x % i === 0) {
                return false;
            }
        }
        return true;
    });
    return arr2;
}

// 测试:
let
    x,
    r,
    arr = [];
for (x = 1; x < 100; x++) {
    arr.push(x);
}
r = get_primes(arr);
if (r.toString() === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].toString()) {
    console.log('测试通过!');
} else {
    console.log('测试失败: ' + r.toString());
}
