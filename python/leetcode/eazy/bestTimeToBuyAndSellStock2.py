#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        if len(prices) < 2:
            return m
        pre = prices[0]
        for i in prices[1:]:
            if i > pre:
                m += i - pre
            pre = i
        return m

    def test(self):
        v = self.maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(v, 7)
        v1 = self.maxProfit([1,2,3,4,5])
        self.assertEqual(v1, 4)
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
