class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        yv=[]
        res=[]
        if numerator==0 or denominator==0:return "0"
        if numerator<0 and denominator<0:
            numerator*=-1
            denominator*=-1
        if numerator<0 :
            yv.append(-1)
            res.append('-')
            numerator*=-1
        if denominator<0:
            yv.append(-1)
            res.append('-')
            denominator*=-1
        
        if numerator>denominator:
            a=numerator%denominator
            b=numerator//denominator
            res.append(str(b))
            numerator=a*10
            if a==0:return ''.join(res)
        else:
            res.append('0')
            numerator*=10
        res.append('.')
        while True:
            a=numerator%denominator
            b=numerator//denominator
            if a==0:
                res.append(str(b))
                return ''.join(res)
            elif numerator in yv:
                res.insert(yv.index(numerator)+2,'(')
                res.append(')')
                return ''.join(res)
            yv.append(numerator)
            numerator=a
            if numerator<denominator:numerator*=10
            res.append(str(b))

        
