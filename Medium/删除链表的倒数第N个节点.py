# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head==None or head.next==None:
            return None
        p=ListNode(None)
        p.next=head
        q=p
        for i in range(n):
            q=q.next
        while q.next!=None:
            q,p=q.next,p.next
        x=p.next
        p.next=p.next.next
        if x==head:
            return x.next
        else:
            return head
        
        
       