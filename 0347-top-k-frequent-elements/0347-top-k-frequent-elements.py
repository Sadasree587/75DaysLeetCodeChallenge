class Solution:
    def topKFrequent(self, nums, k):
        
        from collections import Counter
        
        freq = Counter(nums)
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, count in freq.items():
            bucket[count].append(num)
        
        ans = []
        
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans