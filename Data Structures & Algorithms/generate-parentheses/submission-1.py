class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_p, closed_p = n, n
        res = []
        p_set = []

        def dfs(op, cp):
            if op == 0 and cp == 0:
                res.append(''.join(p_set))
                return

            if op > 0:
                p_set.append("(")
                dfs(op - 1, cp)
                p_set.pop() # MISTAKE: need to pop changes off in order to correctly write data.
            
            if cp > 0 and cp > op: # MISTAKE: cp needs to be greater than op to be placed
                p_set.append(")")
                dfs(op, cp - 1)
                p_set.pop()
        
        dfs(open_p, closed_p)

        return res