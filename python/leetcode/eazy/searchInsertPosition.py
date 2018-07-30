#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype int
        """
        if nums == None or len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def test(self):
        v = self.searchInsert([1], 0)
        self.assertEqual(v, 0)
        v1 = self.searchInsert([1, 3, 5, 6], 5)
        self.assertEqual(v1, 2)
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()

