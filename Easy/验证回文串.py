class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        if not s:
            return True
        s=s.lower()
        pat=r'\w*\w'
        lst=re.findall(pat,s)
        s=''.join(lst)
        #print(s)
        if s==s[::-1]:
            return True
        return False