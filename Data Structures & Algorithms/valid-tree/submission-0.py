class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ad = defaultdict(list)
        visited = set()

        for u, v in edges:
            ad[u].append(v)
            ad[v].append(u)

        print(ad)

        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node)

            for nei in ad[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n

        