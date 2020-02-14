class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        add=1
        for i in range(len(digits)):
            digits[i]=digits[i]+add
            add=digits[i]//10
            digits[i]%=10
            
        if add:
            digits.append(add)
        return digits[::-1]