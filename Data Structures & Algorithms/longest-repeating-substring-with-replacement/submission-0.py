class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr_window = Counter()
        maxf = 0
        res = 0
        l = 0

        for r in range(len(s)):
            curr_window[s[r]] += 1
            maxf = max(maxf, curr_window[s[r]]) # keep track of the highest frequency character

            while (r - l + 1) - maxf > k: # check if the curr window size minus the most frequent character is greater than the total number of replacements
                curr_window[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))


        return res
            
