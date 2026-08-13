class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map_s = dict(Counter(s))
        char_map_t = dict(Counter(t))

        return char_map_s == char_map_t
        