class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Turning the list into a set will eliminate all
        duplicates. 
        Then, we can check the length of the set and 
        the original input. 

        If their lengths are different, then there's a
        duplicate.
        """

        return len(set(nums)) != len(nums)