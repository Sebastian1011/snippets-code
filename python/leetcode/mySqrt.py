#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import math
class Solution(unittest.TestCase):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.floor(math.sqrt(x)))

    def test(self):
        v = self.mySqrt(8)
        self.assertEqual(v, 2)
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()
