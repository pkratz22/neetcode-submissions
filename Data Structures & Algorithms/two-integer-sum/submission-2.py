class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterparts = {}
        for i in range(len(nums)):
            num = nums[i]
            if target-num in counterparts:
                return [counterparts[target-num],i]
            else:
                counterparts[num] = i