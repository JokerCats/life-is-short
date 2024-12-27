// 默认两种循环
let x = 0;
for(i = 1; i <= 100; i++) {
    x += i;
}
console.log(`x : ${x}`);

console.log("----------------")

let o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
// 'name', 'age', 'city'
for (let key in o) {
    if (o.hasOwnProperty(key)) {
        console.log(key);
    }
}

console.log("----------------")

let a = 6;
while (a > 3) {
    console.log(a);
    a--;
}

console.log("----------------")

let b = 6;
do {
    console.log(b);
    b--;
} while (b > 3);