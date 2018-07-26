/**
 * 每个执行上下文都会创建三个重要属性
 * -变量对象 （当前数据作用域）
 * -作用域链
 * -this
 */

// 1、变量对象
 // 全局上下文
 console.log(this);
 console.log(this instanceof Object);

 /**
  * 函数执行上下文过程
  * -进入执行上下文
  * -代码执行
  */
// 进入执行上下文时，内部函数声明已经完成，但是内部变量赋值没有完成，行参赋值已经完成；

function foo(a) {
  var b = 2;
  function c() {}
  var d = function() {};

  b = 3;

}

foo(1);

//进入执行上下文此时
/**
 *AO = {
 *    arguments: {
 *        0: 1,
 *        length: 1
 *    },
 *    a: 1,
 *    b: undefined,
 *    c: reference to function c(){},
 *    d: undefined
 *}
 *
 */

// 进入代码执行阶段
/**
 * AO = {
 *   arguments: {
 *       0: 1,
 *       length: 1
 *   },
 *   a: 1,
 *   b: 3,
 *   c: reference to function c(){},
 *   d: reference to FunctionExpression "d"
 *}
 */

// 2、作用域链
/**
 * 函数创建之后会有一个内部属性[[scope]]，是个数组，在函数创建的时候会保存函数所有父变量对象到其中
 */

 function s(){
     console.log(this['[[scope]]'])
 }
 s();
