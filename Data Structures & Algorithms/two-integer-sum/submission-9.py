class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        2-Sum can be solved using a dictionary with the key-value
        pair of num:[indices]. This dictionary can be created by
        iterating through nums, checking to see if the value is
        already in the dictionary or not. If it is, append the
        current index to the list in the dictionary, otherwise
        create a single-value list with the current index.

        With that dictionary, iterate through nums. For each n,
        find the difference between it and the target, then search
        the dictionary for that difference. If there's no result,
        move on, otherwise select the first element of the list if
        n doesn't happen to equal to the difference. Otherwise,
        the whole list can be returned as is because the question
        condition states that there's only one valid answer.
        """

        # Convert to dict:
        # O(1)
        d = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in d:
                if len(d[n]) < 2:
                    d[n].append(i)
            else:
                d[n] = [i]
        
        # Iterate through the list again and use d as reference
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in d:
                for j in d[diff]:
                    if j > i:
                        return [i,j]