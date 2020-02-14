class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic=defaultdict(list)
        for i in strs:
            dic[tuple(sorted(i))].append(i)
        
        return dic.values()
        


