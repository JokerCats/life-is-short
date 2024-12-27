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




