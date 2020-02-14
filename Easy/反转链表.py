# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        now=head
        if not head:
            return None
        while head.next!=None:
            q=head.next
            head.next=q.next
            q.next=now
            now=q
        return now
            