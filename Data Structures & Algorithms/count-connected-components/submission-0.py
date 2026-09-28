class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        ad = defaultdict(list)
        visited = set()

        for u, v in edges:
            ad[u].append(v)
            ad[v].append(u)

        def bfs(i):
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for nei in ad[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)


        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1

        return res
        
