var v = {
    value: 1
}

function foo(name, age) {
    return {
        name: name,
        age: age,
        value: this.value
    }
}

var fooBind = foo.bind(v, 'Kevin')

console.log(fooBind(18)); // kevin 18
// bind 返回的是新的函数