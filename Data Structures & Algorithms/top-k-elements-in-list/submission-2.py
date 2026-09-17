class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        counts = sorted(dic.items(), key = lambda x: x[1])
        final = []
        for i in range(len(counts)-1, -1, -1):
            if len(final) < k:
                final.append(counts[i][0])
        return final
            
        
        
        
