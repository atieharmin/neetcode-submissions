class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_L = 0
        for a in nums:
            L = 0
            if a-1 not in nums:
                L += 1
                while a+L in nums:
                    L += 1
            max_L = max(L,max_L)
        return max_L

        