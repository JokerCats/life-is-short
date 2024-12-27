// import http from 'http';

var http = require('http');

// 主机名
const hostname = '127.0.0.1';
// 端口号
const port = 3000;

// 创建一个 HTTP 服务器
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, hostname, () => {
    // 通知服务器正在运行
    console.log(`Server running at http://${hostname}:${port}/`);
});