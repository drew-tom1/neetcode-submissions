class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        char_req = dict(Counter(t))
        required, formed = len(char_req.keys()), 0
        valid_chars = defaultdict(int)

        print(required)

        for r in range(len(s)):
            if s[r] in char_req:
                valid_chars[s[r]] += 1
                if char_req[s[r]] == valid_chars[s[r]]:
                    formed += 1
            
            while formed == required:
                if res == "" or len(res) > len(s[l:r + 1]):
                    res = s[l:r + 1]
                if s[l] in valid_chars:
                    valid_chars[s[l]] -= 1
                    if valid_chars[s[l]] < char_req[s[l]]:
                        formed -= 1
                l += 1


        return res
            
            

            

        