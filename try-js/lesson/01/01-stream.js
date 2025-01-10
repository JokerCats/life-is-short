const path = require('path');
const fs = require('fs');

// 获取目标文件路径
const inputPath = path.join(__dirname, '01.jpeg');
const outputPath = path.join(__dirname, '02.jpeg');

const rs = fs.createReadStream(inputPath);
const ws = fs.createWriteStream(outputPath);

rs.pipe(ws);