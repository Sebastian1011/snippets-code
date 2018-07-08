#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t = 0
        for i in range(len(prices) - 1):
            if(prices[i + 1] > prices[i]):
                t += prices[i+1] - prices[i]
        return t


if __name__ == '__main__':
    s = Solution()
    l = [7,1,5,3,6,4]
    t = s.maxProfit(l)
    print(t)