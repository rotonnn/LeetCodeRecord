"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def nxt(self,l):
        if l.left and l.right:
            l.left.next=l.right
            node=l
            while node.next:
                node.right.next=node.next.left
                node=node.next
        
            self.nxt(l.left)
            self.nxt(l.right)
        return 
    def connect(self, root: 'Node') -> 'Node':
        if root:
            self.nxt(root)
        return root