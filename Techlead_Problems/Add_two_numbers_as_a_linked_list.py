#!/usr/bin/env python3
'''
https://www.techseries.dev/products/coderpro/categories/1831147/posts/6176705

  342
+ 465
_____
  807

Below are the linked list representations.
Notice how it's in opposite order.
This is the linked list given as well as the
output that we want.

  2 -> 4 -> 3
+ 5 -> 6 -> 4
_____________
  7 -> 0 -> 8
'''


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def SumLinkedLists(self, a, b):
        initial_sum = a.val + b.val
        if initial_sum > 9:
            list_sum = Node(initial_sum - 10)
            carry = 1
        else:
            list_sum = Node(initial_sum)
            carry = 0
        pt1 = a
        pt2 = b
        while pt1 or pt2:
            new_node_val = pt1 + pt2 + carry


linked_list_a = Node(2)
linked_list_a.next = Node(4)
linked_list_a.next.next = Node(3)

linked_list_b = Node(5)
linked_list_b.next = Node(6)
linked_list_b.next.next = Node(4)
