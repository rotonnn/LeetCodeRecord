class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=[0]
        i,j,add=l1,l2,0
        if not i or not j:
            return 0
        while i or j:
            if i and j:
                res[-1]+=i.val+j.val
                i,j=i.next,j.next
            elif i:
                res[-1]+=i.val
                i=i.next
            else :
                res[-1]+=j.val
                j=j.next
            add=res[-1]//10
            res[-1]%=10
            res.append(add)
        pre=head=ListNode(res[0])
        for i in res[1:-1]:
            now=ListNode(i)
            pre.next=now
            pre=now
        if res[-1]!=0:
            now=ListNode(res[-1])
            pre.next=now
        return head