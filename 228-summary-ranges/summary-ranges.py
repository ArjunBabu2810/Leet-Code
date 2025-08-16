class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        first =nums[0]
        sec = nums[0]
        res = []
        for i in nums[1:]:
            if sec == i-1:
                sec = i
            else:
                if first == sec:
                    res.append(str(first))
                else:
                    res.append(f"{first}->{sec}")
                first=i
                sec=i
        if first == sec:
            res.append(str(first))
        else:
            res.append(f"{first}->{sec}")
        return res
        