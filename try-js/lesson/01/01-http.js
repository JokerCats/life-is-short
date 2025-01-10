const http = require('http');
const path = require('path');
const fs = require('fs');

// 获取目标文件路径
const filePath = path.join(__dirname, 'index.html');

const server = http.createServer((request, response) => {
    // console.log('request', request);

    // console.log('request', getPrototypeChain(request));
    // console.log('response', getPrototypeChain(response));

    // response.end('hello world.');

    const { url, method, headers } = request;

    console.log('url:', url, 'method:', method);
    // console.log('url:', url, 'method:', method, 'headers:', headers);

    if (url === '/' && method === 'GET') {
        fs.readFile(filePath, (err, data) => {
            if (err) {
                response.writeHead(500, {
                    'Content-Type': 'text/plain;charset=utf-8'
                });
                response.end('500 服务器挂了');
                return
            }
            response.statusCode = 200;
            response.setHeader('Content-Type', 'text/html');
            response.end(data);
        });
    } else if (url === '/users' && method === 'GET') {
        response.writeHead(200, {
            'Content-Type': 'application/json'
        });
        response.end(
            JSON.stringify({ name: 'tom' })
        );
    } else if (method === 'GET' && headers.accept.indexOf("image/*") !== -1) {
        const imagePath = path.join(__dirname, url);
        fs.createReadStream(imagePath).pipe(response);
    } else {
        response.statusCode = 404;
        response.setHeader('Content-Type', 'text/plain;charset=utf-8');
        response.end('404 页面未找到');
    }
});
server.listen(3000, () => {
    console.log('Server is listening on port 3000');
});

function getPrototypeChain(obj) {
    const protoChain = [];
    while (obj = Object.getPrototypeOf(obj)) {
        protoChain.push(obj);
    }
    return protoChain;
}