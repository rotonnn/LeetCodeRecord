class Solution:
    def countAndSay(self, n: int) -> str:
        if n==0 :return None
        if n==1:return '1'
        lst='1'
        for i in range(n-1):
            res,j="",0
            while j<len(lst):
                num=1
                while j+1<len(lst) and lst[j]==lst[j+1]:
                    num+=1
                    j+=1
                res+=str(num)+lst[j]
                j+=1
            lst=res
        return lst
        
