class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):return -1
        i,e,tag=1,-1,-1
        while i!=0:
            #print(i)
            if gas[i-1]>=cost[i-1]:
                #print(i,i)
                s=e=i-1
                
                oil=gas[i-1]
                while oil>=cost[s]:
                    oil-=cost[s]
                    s=(s+1)%len(gas)
                    oil+=gas[s]
                    if s==e:return e
                i=(s+1)%len(gas)
            i+=1
        return -1
            
      