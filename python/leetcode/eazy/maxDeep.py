#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        i = 0
        l = [root]
        while l:
            i += 1
            l1 = []
            for n in l:
                if n.left:
                    l1.append(n.left)
                if n.right:
                    l1.append(n.right)
            l = l1
        return i

            

    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
