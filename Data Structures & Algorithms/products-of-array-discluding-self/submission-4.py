class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def get_mul(nums):
            mul = 1
            for num in nums:
                mul *= num
            return mul
        final = []
        total_mul = get_mul(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                new_nums = nums[:i] + nums[i+1:]
                mul = get_mul(new_nums)
                final.append(mul)
                continue
            final.append(int(total_mul/nums[i]))
        return final

        