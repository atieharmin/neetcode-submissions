class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[0 for num in nums]
        suff=[0 for num in nums]
        pref[0] = 1
        suff[-1] = 1
        mul = []
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(len(nums)):
            mul.append(suff[i]*pref[i])
        return mul
        