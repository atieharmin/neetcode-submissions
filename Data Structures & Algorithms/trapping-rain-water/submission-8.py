class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0 for i in range(len(height))]
        suff = [0 for i in range(len(height))]

        ma = 0
        for i in range(1,len(height)):
            ma = max(height[i-1], ma)
            pref[i] = ma
        
        mi = 0
        for i in range(len(height)-2,-1,-1):
            mi = max(height[i+1], mi)
            suff[i] = mi

        water_sum = 0
        for i in range(len(height)):
            w = min(pref[i], suff[i]) - height[i]
            if w > 0:
                water_sum += w
        return water_sum

        


            