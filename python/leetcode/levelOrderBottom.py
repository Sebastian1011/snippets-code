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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        l = [root]
        lRtn = []
        while l:
            lTemp = []
            l1 = []
            for i in l:
                lTemp.append(i.val)
                if i.left:
                    l1.append(i.left)
                if i.right:
                    l1.append(i.right)
            lRtn.append(lTemp)
            l = l1
        lRtn.reverse()
        return lRtn
        

    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        right = root.right
        right.left = TreeNode(15)
        right.right = TreeNode(7)
        v = self.levelOrderBottom(root)
        print(v)
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
