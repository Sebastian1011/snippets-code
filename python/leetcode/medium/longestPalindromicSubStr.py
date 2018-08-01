#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        ml = 0
        ms = ""
        for i in range(len(s)):
            st = s[i]
            if st in d:
                for j in d[st]:
                    if s[j: i + 1] == s[j: i + 1][::-1] and (i - j + 1) > ml:
                        ml = i - j + 1
                        ms = s[j: i + 1]
                d[st].append(i)
            else:
                d[st] = [i]
                if i == 0:
                    ml = 1
                    ms = st
        return ms
            


    def test(self):
        v = self.longestPalindrome("babad")
        self.assertEqual("bab", v)
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
