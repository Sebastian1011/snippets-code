#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = [root]
        deep = 0
        while l:
            deep += 1
            temp = []
            for n in l:
                if n.left == None and n.right == None:
                    return deep
                else:
                    if n.left:
                        temp.append(n.left)
                    if n.right:
                        temp.append(n.right)
            l = temp
        return deep

    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
