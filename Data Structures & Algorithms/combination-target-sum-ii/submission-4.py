class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        candidate_ct = defaultdict(int)
        combination = []
        rt = 0
        res = []

        for i in range(len(candidates)):
            candidate_ct[candidates[i]] += 1

        def dfs(i, total):
            if i >= len(candidates):
                return
            if total > target:
                return
            if candidate_ct[candidates[i]] == -1:
                return
            if total == target:
                if combination not in res:
                    res.append(combination.copy())
                return

            combination.append(candidates[i])
            candidate_ct[candidates[i]] -= 1
            dfs(i, total + candidates[i])

            combination.pop()
            candidate_ct[candidates[i]] += 1
            dfs(i + 1, total)
        
        dfs(0, rt)

        return res


        