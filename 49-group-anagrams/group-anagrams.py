class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            e="".join(sorted(s))
            d[e].append(s)
        
        return list(d.values())
        