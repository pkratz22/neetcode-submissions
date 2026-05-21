class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # [-1,0,1,2,-1,4]
        nums = sorted(nums)
        # [-1,-1,0,1,2,4]
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+= 1
        return res