class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums) # O(n)
        start, end = [], []      
        for num in nums: # O(n)
            if num-1 not in hash_nums:
                start.append(num)
        #    if num+1 not in hash_nums:
        #        end.append(num)
        # nums = [2, 20, 21, 4,10,3,4,5]
        # start = [2, 20, 10]
        # end = [21, 10, 5]
        # set(start + end) = [2,20,10,21,5]
        i = 1
        while start:
            to_pop = []
            for num in start:
                if num+i not in hash_nums:
                    to_pop.append(num)
            for num in to_pop:
                start.remove(num)
            i += 1
        return i-1
