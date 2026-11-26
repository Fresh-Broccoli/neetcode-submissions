class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_volume = 0
        while left < right:
            left_h, right_h = heights[left], heights[right]
            width = right - left
            if left_h > right_h:
                height = right_h
                right -= 1
            else:
                height = left_h
                left += 1
            max_volume = max(max_volume, width*height)
        return max_volume
