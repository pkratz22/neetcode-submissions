class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combos = defaultdict(list)
        for input_str in strs:
            count = [0] * 26
            for c in input_str:
                count[ord(c) - ord("a")] += 1
            combos[tuple(count)].append(input_str)
        return list(combos.values())
