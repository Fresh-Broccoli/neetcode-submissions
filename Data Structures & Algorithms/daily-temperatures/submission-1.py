class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []  # stores indices of unresolved days

        for i, temp in enumerate(temperatures):
            # While current temp is warmer than the temp at the top of the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                output[prev_i] = i - prev_i
            stack.append(i)

        # Any indices still in the stack have no warmer future day → output stays 0
        return output