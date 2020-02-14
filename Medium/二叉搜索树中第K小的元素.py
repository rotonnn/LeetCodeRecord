class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deg=[0]*numCourses
        pre=[[] for _ in range(numCourses)]
        #print(deg,pre)
        lst=[]
        for item in prerequisites:
            deg[item[0]]+=1
            pre[item[1]].append(item[0])
        for i in range(numCourses):
            if deg[i] == 0:
                lst.append(i)
        while lst:
            q=lst.pop(0)
            for ind in pre[q]:  
                deg[ind]-=1
                if deg[ind]==0:lst.append(ind)
        if sum(deg)>0:return False
        else:return True