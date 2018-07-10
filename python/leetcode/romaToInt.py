#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
class Solution(TestCase):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for i in range(len(s)):
            n += self.value_map(s[i]);
            if i > 0 and self.value_map(s[i]) > self.value_map(s[i-1]):
                n = n - 2 * self.value_map(s[i - 1])
        return n


    def value_map(self, k):
        switcher = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        return switcher.get(k, 0)

    def test(self):
        self.assertEqual(self.romanToInt('III'), 3)
        self.assertEqual(self.romanToInt('IV'), 4)
        self.assertEqual(self.romanToInt('LVIII'), 58)

if __name__ == '__main__':
    s = Solution()
    s.test()


        