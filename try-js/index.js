// 获取文件系统模块
var fs = require("fs");

/**
 * 小文件拷贝
 * @param {string} src 原始文件路径
 * @param {string} dst 目标文件路径
 */
function copy(src, dst) {
  // 读取文件内容
  const source = fs.readFileSync(src);
  // 将读取内容写入目标文件
  fs.writeFileSync(dst, source);
}

/**
 * 大文件拷贝
 * @param {string} src 原始文件路径
 * @param {string} dst 目标文件路径
 */
function copy(src, dst) {
  // 一次性将文件写入到内存中会导致内存溢出，因此要细水长流！！
  // 创建只读数据流，通过管道将流连接起来
  fs.createReadStream(src).pipe(fs.createWriteStream(dst));
}

// 获取命令行参数
// process.argv 是一个数组，第一个元素是 node，第二个元素是脚本文件名，从第三个元素开始是运行参数
console.log(process.argv);

function main(argv) {
  copy(argv[0], argv[1]);
}

// main(process.argv.slice(2));
