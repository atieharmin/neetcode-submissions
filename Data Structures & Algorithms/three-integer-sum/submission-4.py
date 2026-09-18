class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            j, k = i+1 , len(nums) -1
            target = -1 * nums[i]
            if nums[i] <= 0:
                while j < k:
                    if nums[j] + nums[k] == target:
                        s = sorted([nums[i],nums[j],nums[k]])
                        if s not in res:
                            res.append(s)
                        k -= 1
                    elif nums[j] + nums[k] < target:
                        j+=1
                    elif nums[j] + nums[k] > target:
                        k-=1
        return res



                

        

                