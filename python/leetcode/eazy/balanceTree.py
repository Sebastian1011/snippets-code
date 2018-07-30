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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isB(root)[0]


    def isB(self, root):
        
        if root == None:
            return (True, 0)
        if root.left == None and root.right == None:
            return (True, 1)
        l = self.isB(root.left)
        r = self.isB(root.right)
        if l[0] == False or r[0] == False:
            return (False, max(l[1], r[1]) + 1)
        if abs(l[1] - r[1]) > 1:
            return (False, max(l[1], r[1]) + 1)
        return (True, max(l[1], r[1]) + 1)


    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
