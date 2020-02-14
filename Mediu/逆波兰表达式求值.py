class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        cal=['+','-','*','/']
        nums=[]
        for i in tokens:
            #print(nums)
            if i=='+':
                a=nums.pop()
                b=nums.pop()
                nums.append(a+b)
            elif i=='-':
                a=nums.pop()
                b=nums.pop()
                nums.append(b-a)
            elif i=='*': 
                a=nums.pop()
                b=nums.pop()
                nums.append(a*b)
            elif i=='/':
                a=nums.pop()
                b=nums.pop()
                nums.append(int(b/a))
            else:
                nums.append(int(i))
        return nums[-1]