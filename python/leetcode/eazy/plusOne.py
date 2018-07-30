#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while digits[i] + 1 > 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 0)
            else:
                i = i - 1
        digits[i] = digits[i] + 1
        return digits


    def test(self):
        v = self.plusOne([1,2,3])
        self.assertEqual(v, [1,2,4])
        v1 = self.plusOne([4,3,2,1])
        self.assertEqual(v1, [4, 3,2,2])
        v2 = self.plusOne([4,3,2,9])
        self.assertEqual(v2, [4, 3,3,0])
        v2 = self.plusOne([9,9,9,9])
        self.assertEqual(v2, [1, 0, 0, 0,0])

        pass

if __name__ == '__main__':
    s = Solution()
    s.test()

