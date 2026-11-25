class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in counts.items():
            buckets[count].append(num)

        output = []
        for ns in buckets[::-1]:
            if len(ns) > 0:
                for n in ns:
                    if k > 0:
                        output.append(n)
                        k -= 1
                    else:
                        return output
        return output
        #print(buckets[-1*k])
