# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre1=ListNode(' ')
        pre2=ListNode(' ')
        pre1.next,pre2.next=l1,l2
        res=head=ListNode(' ')
        while pre1.next and pre2.next:
            if pre1.next.val>pre2.next.val:
                head.next=pre2.next
                pre2.next=pre2.next.next
            else:
                head.next=pre1.next
                pre1.next=pre1.next.next
            head=head.next
        if pre1.next:
            head.next=pre1.next
        if pre2.next:
            head.next=pre2.next
        return res.next