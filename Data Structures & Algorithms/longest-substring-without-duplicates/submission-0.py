class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        while r < len(s):
            if len(s[l:r+1]) == len(set(s[l:r+1])):
                res = max(res,r-l+1)
                r += 1
            else:
                l += 1
        return res
            