class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        prefix.append(1)
        postfix.append(1)

        for i in range(len(nums)-1):
            prefix.append(prefix[i] * nums[i])
            postfix.append(postfix[i] * nums[len(nums)-i-1])
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[len(nums)-i-1])
        
        return res