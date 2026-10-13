class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []

        for i in range(-1000, 1001):
            buckets.append([0, i])
        
        for num in nums:
            buckets[num + 1000][0] += 1
        
        buckets.sort()
        buckets.reverse()

        res = []

        for i in range(k):
            res.append(buckets[i][1])
        
        return res
        