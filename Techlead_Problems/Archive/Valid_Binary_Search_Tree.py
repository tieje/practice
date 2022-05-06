#!/usr/bin/env python3
'''
https://www.techseries.dev/products/coderpro/categories/1831147/posts/6231427
I wrote in my notebook.
My solution:
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def IsValidBSTHelper(self, n, origin, dir):
        if n.left:
            return self.IsValidBSTHelper(n.left, origin, dir)
        if n.right:
            return self.IsValidBSTHelper(n.right, origin, dir)
        if dir == 'right' and origin > n.val:
            return False
        if dir == 'left' and origin < n.val:
            return False
        return True

    def IsValidBST(self, n):
        left = self.IsValidBSTHelper(n.left, n.val, 'left')
        right = self.IsValidBSTHelper(n.right, n.val, 'right')
        return all([left, right])


#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().IsValidBST(node))

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().IsValidBST(node))
# False
'''
My solution is better than the techlead's because
the techlead's solution would fail for BSTs with
depths greater than 3 levels.
'''
