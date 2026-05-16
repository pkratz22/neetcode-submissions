class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        while l < len(heights)-1:
            r = l + 1
            while r < len(heights):
                area = min(heights[l],heights[r]) * (r-l)
                max_area = max(max_area,area)
                r += 1
            l += 1
        return max_area