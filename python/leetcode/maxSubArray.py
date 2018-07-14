#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = 0
        j = 0
        total = 0
        for i in nums:
            total += i
            if total > maxSum:
                maxSum = total
                j = 


    def test(self):
        v = self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(v, 6)
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()

