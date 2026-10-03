class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def has_duplicates(my_list):
            return len(my_list) != len(set(my_list))
        i, j = 0, k if k < len(nums) else len(nums)-1
        found = False
        while j < len(nums):
            found = has_duplicates(nums[i:j+1])
            i, j = i+1, j+1

        return found