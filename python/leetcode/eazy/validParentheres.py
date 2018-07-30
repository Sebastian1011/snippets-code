
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Solution(unittest.TestCase):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        d = len(s)%2
        if d > 0:
            return False
        l = []
        for c in s:
            if self.isLeft(c):
                l.append(c)
            else:
                if len(l) == 0:
                    return False
                p = self.pair_map(c)
                if p == l[-1]:
                    l.pop()
                else:
                    return False
        return len(l) == 0


    def isLeft(self, s):
        v = self.pair_map(s)
        return v == None

    def pair_map(self, s):
        switcher = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        return switcher.get(s, None)

    def test(self):
        self.assertEqual(self.isValid("()"), True)
        self.assertEqual(self.isValid("()[]{}"), True)
        self.assertEqual(self.isValid("([)]"), False)


if __name__ == '__main__':
    s = Solution()
    s.test()
