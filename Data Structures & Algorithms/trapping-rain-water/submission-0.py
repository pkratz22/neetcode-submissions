class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        if not height:
            return res
        l = 0
        r = len(height)-1

        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += max(left_max-height[l],0)
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += max(right_max-height[r],0)
        
        return res