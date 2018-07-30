#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(unittest.TestCase):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            return l2 if l1 == None else l1
        if l1.val > l2.val:
            l0 = l2
            l2 = l2.next
        else:
            l0 = l1
            l1 = l1.next
        l = l0
        while l1 != None or l2 != None:
            if l1 == None or l2 == None:
                l0.next = l1 if l2 == None else l2
                break
            elif l1.val > l2.val:
                l0.next  = l2
                l0 = l0.next
                l2 = l2.next
            else:
                l0.next  = l1
                l0 = l0.next
                l1 = l1.next
        return l

    def test(self):
        list1 = [1, 2, 4]
        list2 = [1, 3, 4]
        l1 = None
        l2 = None
        tmp = None
        for i in list1:
            if l1 == None:
                l1 = ListNode(i)
                tmp = l1
            else:
                tmp.next = ListNode(i)
                tmp = tmp.next
        for j in list2:
            if l2 == None:
                l2 = ListNode(j)
                tmp = l2
            else:
                tmp.next = ListNode(j)
                tmp = tmp.next
        l = self.mergeTwoLists(l1,l2)
        ls = []
        while l != None: 
            ls.append(l.val)
            l = l.next
        self.assertEqual(ls, [1,1,2,3,4,4])
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
