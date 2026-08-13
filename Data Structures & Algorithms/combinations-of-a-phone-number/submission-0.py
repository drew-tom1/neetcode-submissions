class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = { "2": ["a", "b", "c"], "3": ["d", "e", "f"],
                        "4": ["g", "h", "i"], "5": ["j", "k", "l"], 
                        "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                        "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"],}

        res = []
        lc = []

        def dfs(i):
            if not digits:
                return
            if i >= len(digits): # establish base case, boundary check
                res.append(''.join(lc))
                return

            for char in letter_map[digits[i]]:
                
                # since each number has multiple characters, iterate through the char list
                lc.append(char)
                # execute next recursive call with lc having the curr char
                dfs(i + 1)
                # backtrack to then move onto the next char.
                lc.pop()

        dfs(0)

        return res

        