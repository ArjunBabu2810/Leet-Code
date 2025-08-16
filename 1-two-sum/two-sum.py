class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,e in enumerate(nums):
            s = target - e
            if s in d:
                return [d[s],i]
            else:
                d[e]=i