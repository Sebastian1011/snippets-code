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
        cur_min = prices[0]
        for i in range(len(prices)):
            m = max(m, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return m

    def test(self):
        v = self.maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(v, 5)
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
