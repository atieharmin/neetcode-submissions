class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            r = target - nums[i]
            try:
                idr = nums.index(r)
                if i < idr:
                    return [i,idr]
                if i > idr:
                    return [idr, i]
            except:
                continue