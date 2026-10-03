class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-2
        m = arr[-1]
        while i >= 0:
            if arr[i] > m:
                m, arr[i] = arr[i], m
            else:
                arr[i] = m 
            i -= 1
        arr[-1] = -1
        return arr