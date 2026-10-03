class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        return any([k>1 for k in d.values()])