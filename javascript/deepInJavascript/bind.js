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

console.log(fooBind(18));