class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr_window = Counter()
        max_freq = 0
        start = 0
        res = 0

        for end in range(len(s)):
            curr_window[s[end]] += 1

            max_freq = max(max_freq, curr_window[s[end]])

            while (end - start + 1) > max_freq + k:
                curr_window[s[start]] -= 1
                start += 1
            
            res = max(res, end - start + 1)

        return res
            


        