class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        hashmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in hashmap:
                if res and hashmap[c] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return res == []