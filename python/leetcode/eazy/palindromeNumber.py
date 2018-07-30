#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        r = s[::-1]
        for i in range(int(len(s)/2)):
            if r[i] != s[i]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    if s.isPalindrome(-121):
        print('fail')
    else:
        print('pass')
    if s.isPalindrome(121):
        print('pass')
    else:
        print('fail')
        