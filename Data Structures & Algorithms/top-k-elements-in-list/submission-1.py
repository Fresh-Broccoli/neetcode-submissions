class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        buckets = ["-" for _ in range(len(nums)+1)]
        for n, c in counts.items():
            if isinstance(buckets[c], list):
                buckets[c].append(n)
            else:
                buckets[c] = [n]
            
        output = []
        j = -1
        while k > 0:
            if buckets[j] != "-":
                output.extend(buckets[j])
                k -= len(buckets[j])
            j -= 1

        return output