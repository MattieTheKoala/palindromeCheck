# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:43:37 2021

@author: ASUS
"""

class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, n):
        return self._isValidBSTHelper(n, float('-inf'), float('inf'))
    def _isValidBSTHelper(self, n, low, high):
        if not n:
            return True 
            #A null node is a validBST
        val = n.val
        if((val > low and val < high) and self._isValidBSTHelper(n.left, low, val) and self._isValidBSTHelper(n.right, val, high)):
           return True
        return False
#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))



