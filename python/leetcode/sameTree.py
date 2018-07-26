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

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        lp = [p]
        lq = [q]
        i = 0
        while i < len(lp) and i < len(lq):
            if lp[i].val != lq[i].val:
                return False
            if (lp[i].left == None and lq[i].left != None) or (lq[i].left == None and lp[i].left != None):
                return False
            if (lp[i].right == None and lq[i].right != None) or (lq[i].right == None and lp[i].right != None):
                return False
            if lp[i].left != None:
                lp.append(lp[i].left)
                lq.append(lq[i].left)
            if lp[i].right != None:
                lp.append(lp[i].right)
                lq.append(lq[i].right)
            i += 1
        return True

    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
