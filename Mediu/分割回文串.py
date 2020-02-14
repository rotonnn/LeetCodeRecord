class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def findall(s,path):
            if not s:
                res.append(path)
            for i in range(1,len(s)+1):
                tmp=[]
                if s[:i]==s[:i][::-1]:
                    tmp.append(''.join(s[:i]))
                    findall(s[i:],path+tmp)
        findall(list(s),[])
        return res
                