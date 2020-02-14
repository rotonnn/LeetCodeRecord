# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p=head
        lst=[]
        while p and p not in lst :
            lst.append(p)
            p=p.next
        if not p:return False
        return True