class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        # Heap Sort:
        # Time: O(n*log(n))
        # Space: O(1) as it's an in-place algorithm
        def heapify(arr, n, i):
            """Restores the max-heap property for a subtree rooted at index i."""
            largest = i          # Initialize largest as root
            left = 2 * i + 1     # Left child index
            right = 2 * i + 2    # Right child index

            # Check if left child exists and is larger than root
            if left < n and arr[left] > arr[largest]:
                largest = left

            # Check if right child exists and is larger than the current largest
            if right < n and arr[right] > arr[largest]:
                largest = right

            # Change root if a child was larger
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # Swap

                # Recursively heapify the affected sub-tree
                heapify(arr, n, largest)

        def heap_sort(arr):
            """Sorts an array in ascending order using Heap Sort."""
            n = len(arr)

            # Phase 1: Build a max heap (rearrange array)
            # Start from the last non-leaf node and move upwards
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            # Phase 2: Extract elements from the heap one by one
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
                heapify(arr, i, 0)               # Call max heapify on the reduced heap

            return arr

        # sorted_nums = [-4,-1,-1,0,1,2]
        # No need to check nums length as it's guaranteed to be greater or equal to 3
        sorted_nums = heap_sort(nums)
        output = []
        i = 0
        while i < len(sorted_nums)-2:
            j, k = i + 1, len(sorted_nums)-1
            while j < k:
                s = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    output.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    while j < k and sorted_nums[j] == sorted_nums[j + 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            while i < k and sorted_nums[i] == sorted_nums[i+1]:
                i += 1
            i += 1
        return output