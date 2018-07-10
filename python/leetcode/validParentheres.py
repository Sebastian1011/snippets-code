
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
        print('d is : ', d)
        if d > 0:
            return False
        l = len(s)
        for i in range(int(l/2)):
            c = s[i]
            p = self.pair_map(c)
            if s[ l - 1 - i] != p:
                return False
        return True
        
    def pair_map(self, s):
        switcher = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        return switcher.get(s, None)

    def test(self):
        self.assertEqual(self.isValid("()"), True)
        self.assertEqual(self.isValid("()[]{}"), True)
        self.assertEqual(self.isValid("([)]"), False)

if __name__ == '__main__':
    s = Solution()
    s.test()
