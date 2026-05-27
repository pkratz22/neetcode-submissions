class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [0] * len(nums)
        right_prod = [0] * len(nums)
        res = [0] * len(nums)
        left = 1
        right = 1
        
        for i in range(len(nums)):
            left_prod[i] = left
            left *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            right_prod[i] = right
            right *= nums[i]
        for i in range(len(nums)):
            res[i] = left_prod[i] * right_prod[i]
        return res