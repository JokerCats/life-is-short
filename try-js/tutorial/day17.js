'use strict';

const fs = require('fs');
const path = require('path');

function travel(dir, callback) {
    fs.readdirSync(dir).forEach(
        function(file) {
            const filePath = path.join(dir, file);
            if(fs.statSync(filePath).isDirectory()) {
                travel(filePath, callback);
            } else {
                callback(filePath);
            }
        }
    );
}

travel('.', function(filePath) {
    console.log(filePath);
})