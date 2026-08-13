class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        char_req = dict(Counter(t))
        required, formed = len(char_req.keys()), 0
        valid_chars = defaultdict(int)

        for r in range(len(s)):
            # if newest char is one of the chars in t, add to dict, if freq is satisfied, increment the number of chars satisfied
            if s[r] in char_req:
                valid_chars[s[r]] += 1
                if char_req[s[r]] == valid_chars[s[r]]:
                    formed += 1
            # once there are enough chars of the right frequency in the window, begin shrinking
            while formed == required:
                # if initial substring or if smaller length, reassign to smaller length
                if res == "" or len(res) > len(s[l:r + 1]):
                    res = s[l:r + 1]
                # remove the char and decrement frequency, if decremented past the needed freq, decrement the total number of chars satisfied
                if s[l] in valid_chars:
                    valid_chars[s[l]] -= 1
                    if valid_chars[s[l]] < char_req[s[l]]:
                        formed -= 1
                l += 1


        return res
            
            

            

        