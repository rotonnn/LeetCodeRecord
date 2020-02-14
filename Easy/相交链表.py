# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headB==None or headB==None:return None
        count=0
        q,p=headA,headB
        while q!=None and p!=None:
            q=q.next
            p=p.next
        if q:
            while q!=None:
                q=q.next
                count+=1
            q,p=headA,headB
            while count!=0:
                q=q.next
                count-=1
        else:
            while p!=None:
                p=p.next
                count+=1
            q,p=headA,headB
            while count!=0:
                p=p.next
                count-=1
        while p!=None and q!=None:
            if p==q:
                return p
            p=p.next
            q=q.next
        return None
            