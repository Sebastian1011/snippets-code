#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre = []
        for i in range(rowIndex + 1):
            if i < 1:
                pre = [1]
            else:
                temp = [1]
                for n in range(len(pre) - 1):
                    temp.append(pre[n] + pre[n + 1])
                temp.append(1)
                pre = temp
        return pre
        

    def test(self):
        v = self.getRow(5)
        print(v)
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
