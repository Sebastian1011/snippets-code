// 为了测试原型链，学习了解
function Person(){}
Person.prototype.name = "Hello"

var person = new Person()
var person1 = new Person()

console.log('person name: ', person.name)
console.log('person1 name: ', person1.name)

console.log('person prototype === Person.prototype:', person.prototype === Person.prototype)
console.log('person __proto__ === Person.prototype:', person.__proto__ === Person.prototype)

console.log('Person :', Person)
console.log('person prototype :', person.prototype)
console.log('person __proto__ :', person.__proto__)

/*** 
 * 结论：
 * Person 是构造函数
 * Person 的 prototype 是调用 Person 函数创建的实例的原型
 * 即 Person.prototype 是 person 和 Person1 的原型
 ***/