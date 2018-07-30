#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        for i in range(numRows):
            if i < 1:
                l.append([1])
            else:
                temp = [1]
                pre = l[i - 1]
                for n in range(len(pre) - 1):
                    temp.append(pre[n] + pre[n + 1])
                temp.append(1)
                l.append(temp)
        return l
        

    def test(self):
        v = self.generate(5)
        print(v)
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
