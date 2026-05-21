class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if num-1 in nums:
                continue
            else:
                counter = 1
                while num+counter in nums:
                    counter += 1
                res = max(res,counter)
        return res