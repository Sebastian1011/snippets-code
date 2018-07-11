#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            j = i
            for n in nums[i+1:]:
                j += 1
                r = nums[i] + n
                if(r == target):
                    return [i, j]

        

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    r = s.twoSum(nums, target)
    print(r)
