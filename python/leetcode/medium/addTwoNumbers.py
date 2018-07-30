#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(unittest.TestCase):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        ln = None
        increase = 0
        while l1 != None or l2 != None:
            v = increase
            if l1 != None:
                v += l1.val
                l1 = l1.next
            if l2 != None:
                v += l2.val
                l2 = l2.next
            if v > 9:
                v = v - 10
                increase = 1
            else:
                increase = 0
            
            if ln:
                ln.next = ListNode(v)
                ln = ln.next
            else:
                ln = ListNode(v)
                head = ln
        if increase > 0:
            ln.next = ListNode(increase)
        return head


    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
