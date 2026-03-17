class Solution:
    def topKFrequent(self, nums, k):
        
        from collections import Counter
        import heapq
        
        freq = Counter(nums)
        
        heap = []
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        
        while heap:
            ans.append(heapq.heappop(heap)[1])
        
        return ans 