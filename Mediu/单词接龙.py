class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        if  not (beginWord or endWord or wordList):return 0
        dic=defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                cur=list(i)
                cur[j]='*'
                cur=''.join(cur)
                dic[cur].append(i)
        step,q=0,[]
        for i in range(len(beginWord)):
            cur=list(beginWord)
            cur[i]='*'
            cur=''.join(cur)
            if dic[cur]:
                q+=dic[cur]
                dic.pop(cur)
        def bfs(endWord,q,dic,step):
            if endWord in q:
                return step+1
            tmp=[]
            while q:
                for i in range(len(q[0])):
                    cur=list(q[0])
                    cur[i]='*'
                    cur=''.join(cur)
                    if dic[cur]:
                        tmp+=dic[cur]
                        dic.pop(cur)
                q.pop(0)
            return bfs(endWord,tmp,dic,step+1) if tmp else 0
        return bfs(endWord,q,dic,1)