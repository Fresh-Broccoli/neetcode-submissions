class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(lst, i, j, target) -> int:
            if i > j:
                return -1
            mid = (i+j)//2

            if lst[mid] > target:
                return binary_search(lst, i, mid - 1, target)
            elif lst[mid] < target:
                return binary_search(lst, mid + 1, j, target)
            return mid

        return binary_search(nums, 0, len(nums)-1, target)