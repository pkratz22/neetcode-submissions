class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            end = start + 1
            while s[end] != "#":
                end += 1
            string_length_chars = s[start:end]
            print(string_length_chars)
            string_length = int(string_length_chars)
            string = s[end+1:end+1+string_length]
            res.append(string)
            start = end + 1 + string_length
        return res