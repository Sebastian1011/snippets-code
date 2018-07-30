#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(unittest.TestCase):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        s = [(p, q)]
        while s:
            cur_p, cur_q = s.pop()
            if (cur_p is None) ^ (cur_q is None):
                return False
            if cur_p is None or cur_q is None:
                continue
            if cur_p.val != cur_q.val:
                return False
            s.append((cur_p.left, cur_q.right))
            s.append((cur_p.right, cur_q.left))
        return True


    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
