class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            e=str(sorted(s))
            if e in d:
                d[e].append(s)
            else:
                d[e]=[s]
        res = []

        for k in d:
            res.append(d[k])
        return sorted(res,key=len)
        