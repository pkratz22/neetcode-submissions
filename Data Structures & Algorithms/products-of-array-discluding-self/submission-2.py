class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        res.append(1)
        post = 1

        for i in range(len(nums)-1):
            res.append(res[i] * nums[i])
        for i in range(len(nums)): # i: 0 --> 1 --> 2 --> 3
            print(i)
            res[len(nums)-i-1] *= post
            post *= nums[len(nums)-i-1]
        return res


# res = [1,1,2,8]

# i = 0
    # res[3] *= 1 --> res = [1,1,2,8]
    # post = 1 * 6 = 6
# i = 1
    # res[2] *= 6
    # post = 6 * 4 = 24
# i = 2
    # res[1] *= 24
    # post = 24 * 2 = 48
# i = 3
    # res[0] *= 48
    