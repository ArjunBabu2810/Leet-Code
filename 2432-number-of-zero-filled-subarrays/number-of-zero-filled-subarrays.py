class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        sub = 0
        for n in nums:
            if n==0:
                sub+=1
                c+=sub
            else:
                sub=0
        return c
            