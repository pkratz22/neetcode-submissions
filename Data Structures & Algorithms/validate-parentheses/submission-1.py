class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        hashmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for character in s:
            if character == "(" or character == "{" or character == "[":
                res.append(character)
            elif res == [] or hashmap[character] != res.pop():
                return False
            else:
                continue
        return res == []