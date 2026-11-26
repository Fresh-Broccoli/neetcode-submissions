class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        output = 0
        for n in lookup:
            if n-1 not in lookup:
                count = 1
                tn = n
                while tn+1 in lookup:
                    count += 1
                    tn += 1
                output = max(output, count)
        return output

