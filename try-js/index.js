"use strict";

let user = {
    name: 'John',
    age: 30,
    // [fruit]: 5, // 计算属性
};

for (const key in user) {
    if (Object.prototype.hasOwnProperty.call(user, key)) {
        const element = user[key];
        console.log('element:', element);
    }
}