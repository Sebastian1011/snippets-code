#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        s = strs[0]
        for str in strs:
            if len(s) > len(str):
                s = str
        prefix = ""
        for i in range(len(s)):
            c = s[i]
            for str in strs:
                if str[i] != c:
                    return prefix
            prefix += c
        return prefix

    def test(self):
        self.assertEqual(self.longestCommonPrefix(["flower","flow","flight"]), 'fl')
        self.assertEqual(self.longestCommonPrefix(["dog","racecar","car"]), '')
        self.assertEqual(self.longestCommonPrefix(["","b"]), '')


if __name__ == '__main__':
    s = Solution()
    s.test()

