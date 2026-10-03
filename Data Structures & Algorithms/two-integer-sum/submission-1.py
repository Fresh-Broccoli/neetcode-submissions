class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = self.create_val_to_dex_dict(nums)
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in d and i != d[diff]:
                return [i, d[diff]]
        return []

    def create_val_to_dex_dict(self, nums):
        return {nums[i]: i for i in range(len(nums))}
