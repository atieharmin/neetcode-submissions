class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        n_zero = nums.count(0)
        if n_zero > 1:
            return [0 for i in range(len(nums))]
        
        for num in nums:
            if n_zero == 1 and num == 0:
                continue
            mul *= num
        
        final = []
        if n_zero == 1:
            for num in nums:
                if num == 0:
                    final.append(mul)
                else:
                    final.append(0)
            return final
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                final.append(mul)
                continue
            final.append(int(mul/nums[i]))
        return final

        