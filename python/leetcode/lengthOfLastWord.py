#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = s.split(" ")
        j = len(ls) - 1
        while j >= 0:
            l = len(ls[j])
            if l > 0:
                return l
            j -= j
        return 0

    def test(self):
        v = self.lengthOfLastWord("Hello World")
        self.assertEqual(v, 5)
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()

