class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(lst, i, j, target) -> int:
            if i > j:
                return -1
            mid = (i+j)//2
            print("mid:", mid)
            print("mid num:", lst[mid])
            print('i', i)
            print('j', j)
            if lst[mid] > target:
                return binary_search(lst, i, mid - 1, target)
            elif lst[mid] < target:
                return binary_search(lst, mid + 1, j, target)
            return mid

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        return binary_search(nums, 0, len(nums)-1, target)