class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums =          [1,   2, 4, 6]
        # left_product =  [1,   1, 2, 8]
        # right_product = [48, 24, 6, 1]
        # output =        [48, 24, 12, 8]
        left_product, right_product = [1 for _ in range(len(nums))], [1 for _ in range(len(nums))]
        for i in range(1, len(left_product)):
            left_product[i] = left_product[i-1]*nums[i-1]
        for j in range(len(right_product)-2,-1,-1): # Iterate backwards
            right_product[j] = right_product[j+1]*nums[j+1]
        #print("left_product:", left_product)
        #print("right_product:", right_product)
        return [left_product[i]*right_product[i] for i in range(len(nums))]