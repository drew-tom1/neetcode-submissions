class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ad = defaultdict(list)

        for u, v in edges:
            ad[u].append(v)
            ad[v].append(u)

        cycleStart = -1
        visited = set()
        cycle = set()

        def dfs(node, par):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)
            for nei in ad[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        
        return []

        