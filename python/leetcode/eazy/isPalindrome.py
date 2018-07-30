#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0 :
            return None
        if l == 1: 
            return nums[0]
        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums [-2]:
            return nums[-1]
        for i in range(1, l - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
        return None

    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
