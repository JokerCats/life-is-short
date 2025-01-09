const bin = new Buffer([0x68, 0x65, 0x6c, 0x6c, 0x6f]);
const dup = new Buffer(bin.length);

console.log("bin : " + bin);

bin.copy(dup);
console.log("dup : " + dup);
console.log("---------------");

dup[0] = 0x48;

console.log("bin : " + bin);
console.log("dup : " + dup);
console.log("---------------");

let str = bin.toString('utf-8');
console.log("str : " + str);

let convertBin = new Buffer('hello', 'utf-8');
console.log("convert bin : ", convertBin);

let slice = bin.slice(2);
console.log(slice);