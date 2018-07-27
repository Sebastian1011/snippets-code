#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(unittest.TestCase):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            mid = int((len(nums) - 1)/2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0: mid])
            root.right = self.sortedArrayToBST(nums[mid + 1: len(nums)])
            return root
        else:
            return None
    

    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
