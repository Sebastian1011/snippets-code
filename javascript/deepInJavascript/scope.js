
var scope = "global scope"

function checkScope(){
    var scope = 'local scope';
    function f(){
        return scope;
    }
    return f();
}

function checkScope1(){
    var scope = 'local scope';
    function f() {
        return scope;
    }
    return f;
}

var v = checkScope();
var v1 = checkScope1()();
console.log('v : ', v);
console.log('v1 : ', v1);