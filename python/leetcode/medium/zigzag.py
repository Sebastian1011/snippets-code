#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Solution(unittest.TestCase):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or len(s) < numRows:
            return s
        i = 0
        d = [""] * numRows
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    d[j] += s[i]
                    i += 1
                else:
                    return "".join(d)
            for m in range(1, numRows - 1):
                if i < len(s):
                    d[numRows - 1 - m] += s[i]
                    i += 1
                else:
                    return "".join(d)
        return "".join(d)


    def test(self):
        v = self.convert("PAYPALISHIRING", 3)
        self.assertEqual(v, "PAHNAPLSIIGYIR")
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
