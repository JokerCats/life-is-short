// JS 中并不区分类和实例，万物皆实例。因此创建一个对象的本质是原型的指向转移。
let Student = {
    name: "Robot",
    skill: function () {
        console.log(`${this.name} is running ..`);
    }
}

let Bird = {
    name: "pigeon",
    skill: function () {
        console.log(`${this.name} is flying ..`);
    }
}

function create(name) {
    let s = Object.create(Bird);
    s.name = name;
    return s;
}

let stu = create("Joker");
stu.skill();