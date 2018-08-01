#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        str = ''
        for c in s:
            str = str.split(c)[-1] + c
            l = max(len(str), l)
        return l


    def test(self):
        v = self.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, v)
        v = self.lengthOfLongestSubstring("bbbb")
        self.assertEqual(1, v)
        v = self.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, v)
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
