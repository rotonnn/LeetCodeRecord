# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return
        n=len(lists)
        return self.merge(0,n-1,lists)
    def merge(self,left,right,lists):
        if left==right:
            return lists[left]
        mid=(left+right)//2
        l=self.merge(left,mid,lists)
        r=self.merge(mid+1,right,lists)
        return self.merge2(l,r)
    def merge2(self,l,r):
        if not l:return r
        if not r:return l
        while l and r:
            if l.val>=r.val:
                r.next=self.merge2(l,r.next)
            elif l.val<r.val:
                l.next=self.merge2(l.next,r)
            return l if l.val<r.val else r
        
        
        