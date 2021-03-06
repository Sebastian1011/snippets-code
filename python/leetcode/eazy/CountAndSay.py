#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        while n > 1:
            s = self.getNext(s)
            n -= 1
        return s
    
    def getNext(self, s):
        tmp = '' 
        r = ''
        i = 0
        for c in s:
            if tmp == '':
                tmp = c
            if c != tmp:
                r = r + str(i) + tmp
                tmp = c
                i = 1
            else:
                i += 1
        r = r + str(i) + tmp
        return r
        
    def test(self):
        v5 = self.countAndSay(5)
        self.assertEqual(v5, '111221')
        v6 = self.countAndSay(6)
        self.assertEqual(v6, "312211")
        pass

if __name__ == '__main__':
    s = Solution()
    s.test()
