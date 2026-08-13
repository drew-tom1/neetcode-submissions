class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum(): #if s[l] is not alphanumeric
                l += 1
            elif not s[r].isalnum(): #if s[r] is not alphanumeric
                r -= 1
            elif s[r].lower() == s[l].lower(): #if they are equal, increment both pointers
                l += 1
                r -= 1
            else: # if none of this logic holds, i.e. letters are NOT equal.
                return False
        return True
        