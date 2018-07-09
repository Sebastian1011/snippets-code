#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fibonacci;
# 递归实现
def fib(n):
    print('Cal fib: ', n)
    if n <= 0:
        return 0
    if n == 1: 
        return 1
    return fib(n-2) + fib(n-1)

def fibTop(n, m):
    if m[n] != -1:
        return m[n]
    print('cal: ', n)
    if n<=2:
        m[n] = 1
    else:
        m[n] = fibTop(n-1, m) + fibTop(n-1, m)
    return m[n]

def fibonacci(n):
    if n<=0: 
        return 0
    memo = []
    for i in range(n + 1):
        memo.append(-1)
    return fibTop(n, memo)



if __name__ == '__main__':
    print('dynamic programming.')
    # cur = fib(6);
    value = fibonacci(6)
    print('result: ', value)