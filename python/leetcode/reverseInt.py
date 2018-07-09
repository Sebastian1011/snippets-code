#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        pre = 1
        if x < 0: 
            pre = -1
        s = str(abs(x))
        r = ""
        for c in s:
            r = c + r
        if r[0] == '0':
            r = r[1:]
        r = pre * int(r)
        if r > (2**31 - 1) or r < -2**31:
            return 0
        return r
        


if __name__ == '__main__':
    s = Solution()
    r = s.reverse(123)
    if r == 321:
        print('pass')
    else:
        print('fail')
    r = s.reverse(-123)
    if r == -321:
        print('pass')
    else:
        print('fail')
    r = s.reverse(120)
    if r == 21:
        print('pass')
    else:
        print('fail')