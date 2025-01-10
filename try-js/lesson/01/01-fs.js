import path from 'path';
import fs from 'fs';

// 获取目标文件路径
const filePath = path.join(__dirname, 'conf.js');

// 同步调用
const data = fs.readFileSync(filePath, 'utf-8');
console.log('同步读取结果\n' + data);
console.log('===========================');

// 异步调用
// 错误优先的回调
// ns * 1000 => ms
fs.readFile(filePath, (err, data) => {
    if(err) {
        throw err;
    }
    console.log('异步读取结果\n' + data.toString());
    console.log('===========================');
});

// promise
const callPromise = async() => {
    const { promisify } = require("util");
    const readFile2 = promisify(fs.readFile);
    const data = await readFile2(filePath);
    console.log('promise读取结果\n' + data);
}
callPromise();