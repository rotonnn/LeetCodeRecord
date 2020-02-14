# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head :return 
        val=[]
        while head:
            val.append(head.val)
            head=head.next
        lst=sorted(val)
        res=h=ListNode(lst[0])
        for i in lst[1:]:
            h.next=ListNode(i)
            h=h.next
        h.next=None
        return res