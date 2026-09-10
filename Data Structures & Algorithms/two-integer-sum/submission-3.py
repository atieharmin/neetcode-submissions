class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {value: i for i,value in enumerate(nums)}

        for i in range(len(nums)):
            r = target - nums[i]
            try:
                idr = dic[r]
                if i < idr:
                    return [i,idr]
                if i > idr:
                    return [idr, i]
            except:
                continue