#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = 0
        cur = 1
        for i in range(n):
            temp = cur
            cur += pre
            pre = temp
        return cur

    def test(self):
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()

