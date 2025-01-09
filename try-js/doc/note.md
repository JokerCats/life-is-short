# NodeJS

### 基础概念

定义：JS 解析器 **（运行环境）**

用途：操作磁盘文件 **（fs）** 或搭建服务器 **（http）**

权限：使用 NodeJS 监听 80 或 443 端口提供 HTTP（s）服务时需要 root 权限。

模块化：[CMD](http://wiki.commonjs.org/) 模块系统，主模块作为程序入口，所有模块在运行时仅初始化一次。

- require
    > 用于在当前模块加载和使用别的模块，传入一个模块名并返回一个模块导出对象。

- exports
    > 用于导出模块公有方法和属性。

- module
    > 用于替换当前模块的导出对象。

二进制模块：由 C/C++ 编写，编译好后的扩展名为 `.node` 且使用方式与 JS 模块相同。

### 组织和部署

模块路径解析规则

  - 内置模块：不做路径解析，直接传递内部模块的导出对象。

    ```js
    var http = require('http');
    ```

  - node_modules：用于存放模块，NodeJS 会依次查询路径。

  - NODE_PATH：与系统环境变量类似，用于指定额外的查询路径。

package（模块的集合）

  - index.js
    ```js
    // 以下两条语句等价
    var cat = require('home/user/lib/cat');
    var cat = require('home/user/lib/cat/index')
    ```

  - package.json：用于自定义入口模块的文件名与存放位置。
    ```json
    - /home/user/lib/
    - cat/
        + doc/
        - lib/
            head.js
            body.js
            main.js
        + tests/
        package.json

    {
      "name": "cat",
      "main": "./lib/main.js"
    }
    ```

版本号含义（X.Y.Z）

  - Z：修复 Bug
  - Y：追加了新功能，但向下兼容
  - X：重构改版功能，但不向下兼容

### 文件操作

Buffer 对象用来提供对二进制数据的操作，与字符串类似。

字符串是只读的，因此对它修改会生成一个新的字符串，原字符串保持不变。

Buffer 类似可做指针操作的 C 语言数组，修改会影响原 Buffer 对象。

> 如果想对 Buffer 进行拷贝
> 1. 创建一个新的 Buffer 对象
> 2. 使用 copy 方法将数据复制过去。

Stream 基于事件机制，所有 Stream 实例都继承于 EventEmitter。

> 常见事件（读）
> - open：当文件被打开时触发。
> - data：当有数据可读时触发。
> - end：当数据读取完毕时触发。
> - close：当文件被关闭时触发。
> - error：当发生错误时触发。
> - readable：当流有数据可读时触发，但不会自动读取数据。需要手动调用 read() 方法。
> - pause：当流被暂停时触发。
> - resume：当流恢复时触发。
>
> 常见事件（写）
> - open：当文件被打开时触发。
> - close：当文件被关闭时触发。
> - finish：当所有数据已被写入到底层系统时触发。
> - error：当发生错误时触发.
> - pipe：当有数据通过管道传输到写入流时触发。
> - unpipe：当管道传输被解除时触发。
> - drain：当写入缓冲区被排空时触发，可以继续写入数据。

Path 简化路径相关操作

> path.normalize 将路径转换为标准路径。
> path.join 将多个路径拼接为标准路径。
> path.extname 获取文件扩展名。


