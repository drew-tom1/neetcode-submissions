class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        normalized = ""
        for char in s:
            if char.isalnum():
                normalized += "" + char
        return normalized[::-1] == normalized

        