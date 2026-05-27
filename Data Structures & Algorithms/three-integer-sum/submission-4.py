class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        # -1,-1,0,1,2,4
        i = 0
        while i < len(nums)-2:
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i+=1
        return res