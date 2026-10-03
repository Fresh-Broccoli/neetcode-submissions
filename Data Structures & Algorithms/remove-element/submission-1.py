class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        max_len, i, k = len(nums), 0, 0
        while i < max_len-k:
            #print("nums[i]:",nums[i])
            if nums[i] == val:
                print("Popped:", nums.pop(i))
                k += 1
            else:
                i += 1
            #print("nums:", nums)
            #print(k)
        #print("Final Nums:", nums)
        return max_len-k