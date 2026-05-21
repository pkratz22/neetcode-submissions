class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        min_border = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                max_left[i] = height[i]
            else:
                max_left[i] = max(max_left[i-1],height[i])
        for i in range(len(height)-1,0,-1):
            if i == len(height)-1:
                max_right[i] = height[i]
            else:
                max_right[i] = max(max_right[i+1],height[i])
        for i in range(len(height)):
            min_border[i] = min(max_left[i],max_right[i])
        for i in range(len(height)):
            res += max(min_border[i]-height[i],0)
        return res