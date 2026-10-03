class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(lst: List[int], low, high, target) -> int:
            # O(log(n))
            if low > high:
                return -1
            
            mid = (low + high)//2

            if lst[mid] > target:
                return binary_search(lst, low, mid-1, target)

            elif lst[mid] < target:
                return binary_search(lst, mid+1, high, target)
            else:
                return mid

        def between(target, low, high):
            return low <= target <= high

        def equal_or_greater_binary_search(lst: List[List[int]], low, high, target, ) -> int:
            if low > high:
                return -1
            
            mid = (low + high)//2

            if lst[mid][0] > target:
                return equal_or_greater_binary_search(lst, low, mid-1, target)
            elif lst[mid][0] < target:
                if lst[mid][-1] >= target:
                    return mid
                return equal_or_greater_binary_search(lst, mid+1, high, target)
            else:
                return mid

        target_row = equal_or_greater_binary_search(matrix, 0, len(matrix)-1, target)

        if target_row > -1:
            return binary_search(matrix[target_row], 0, len(matrix[target_row])-1, target) > -1
        else:
            return False


        return two_d_binary_search(matrix, 0, len(matrix)-1, 0, len(matrix[0]-1)-1, target)