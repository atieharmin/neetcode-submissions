class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        height = min(heights[start],heights[end])
        width = end - start
        max_s = height * width
        while start < end:
            height = min(heights[start],heights[end])
            width = end - start
            s = height * width
            if s > max_s:
                max_s = s
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return max_s





        