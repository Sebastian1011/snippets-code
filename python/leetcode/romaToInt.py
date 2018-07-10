#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for i in range(len(s)):
            n += self.value_map(s[i]);
            if i > 0 and self.value_map(s[i]) > self.value_map(s[i-1]):
                n = n - 2 * self.value_map(s[i - 1])
        return n


    def value_map(self, k):
        switcher = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        return switcher.get(k, 0)


if __name__ == '__main__':
    s = Solution()
    v1 = s.romanToInt('III')
    if v1 == 3:
        print('pass')
    else:
        print('fail')
    v2 = s.romanToInt('IV')
    if v2 == 4:
        print('pass')
    else:
        print('fail')
    v3 = s.romanToInt('LVIII')
    if v3 == 3:
        print('pass')
    else:
        print('fail')


        