class Solution:
    def myAtoi(self, str: str) -> int:
        s=str.lstrip()
        s = re.findall(r'^[+\-]?\d+', s)
        string = ''.join(s)
        if not string:
            return 0
        n = int(string)

        return min(max(n,-2**31),2**31-1)