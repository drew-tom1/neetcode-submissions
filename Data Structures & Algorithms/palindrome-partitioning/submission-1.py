class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substrings = []

        # make a palindrome check
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # recursive call
        def dfs(start):
            if start == len(s):
                res.append(substrings.copy())
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    substrings.append(s[start : end + 1])
                    dfs(end + 1)
                    substrings.pop()

        dfs(0)

        return res
        