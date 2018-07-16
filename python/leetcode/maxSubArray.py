#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxCurrent = nums[0]
        maxRtn = nums[0]
        i = 1
        while i < len(nums):
            maxCurrent = max(nums[i] , nums[i] + maxCurrent)
            maxRtn = max(maxRtn, maxCurrent)
            i += 1
        return maxRtn



    def test(self):
        v = self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(v, 6)
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()

