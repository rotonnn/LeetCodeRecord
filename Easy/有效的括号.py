class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        dic = {'}': '{', ')': '(', ']': '['}
        lst=[]
        for i in s:
            if i in dic.values():
                lst.append(i)
            else:
                if not lst:
                    return False
                out = lst.pop()
                if dic[i] != out:
                    return False
        if lst:
            return False
        return True