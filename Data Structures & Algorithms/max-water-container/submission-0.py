class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculate_water(i,j):
            return min(heights[i], heights[j]) * (j - i)
        i,j = 0,len(heights)-1
        most_water = 0
        while i < j:
            water = calculate_water(i,j)
            if water > most_water:
                most_water = water
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return most_water