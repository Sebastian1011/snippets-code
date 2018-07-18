#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
        

    def test(self):
        v = self.addBinary("11", "1")
        self.assertEqual(v, "100")
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()

