class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        for num in nums:
            if num-1 not in nums:
                i = 1
                while num + i in nums:
                    i += 1
                max_streak = max(max_streak,i)
        return max_streak
                
# [2,20,4,10,3,4,5]


# num = 2
#   i = 1
#   i = 2
#   i = 3
#
#
#
#
#
#
#
#
#
#