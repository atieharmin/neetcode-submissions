class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(list)
        counts = defaultdict(int)
        freqs = [[] for i in range(len(nums))]
        final = []
        for num in nums:
            counts[num] += 1
        for a,b in counts.items():
            freqs[b-1].append(a)
        for i in range(len(freqs)-1, -1, -1):
            if len(final) < k:
                final+=freqs[i]
            
        return final