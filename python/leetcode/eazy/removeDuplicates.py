#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < (len(nums) -1):
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
            else: 
                i = i + 1
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    l = [0, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8]
    n = solution.removeDuplicates(l)
    print("len is : ", n)
    print('l is : ', l)
