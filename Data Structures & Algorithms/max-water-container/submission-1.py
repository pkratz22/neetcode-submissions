class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area,area)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                if heights[l+1] > heights[r-1]:
                    r -= 1
                else:
                    l += 1
        return max_area

#[1,7,2,5,4,7,3,6]
# 0,7 --> 1*6 = 6
