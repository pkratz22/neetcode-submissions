class Solution:
    def isPalindrome(self, s: str) -> bool:
        point_a = 0
        point_b = len(s)-1
        while point_a < point_b:
            if not s[point_a].isalnum():
                point_a += 1
                continue
            if not s[point_b].isalnum():
                point_b -= 1
                continue
            if s[point_a].lower() != s[point_b].lower():
                return False
            point_a += 1
            point_b -= 1
        return True