class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) > 1:
                mid = len(nums)//2
                left = merge_sort(nums[0:mid])
                right = merge_sort(nums[mid:])
                i, j = 0, 0
                out = []
                
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        out.append(left[i])
                        i += 1
                    else:
                        out.append(right[j])
                        j += 1
                if j >= len(right):
                    out.extend(left[i:])
                else:
                    out.extend(right[j:])
                return out
            else:
                return nums
        return merge_sort(nums)
            