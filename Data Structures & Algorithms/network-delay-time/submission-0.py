class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        ad = defaultdict(list)
        visited = set()
        dist = {num + 1: float("inf") for num in range(n)}
        dist[k] = 0
        mheap = []
        heapq.heappush(mheap, (0, k))

        for f, t, c in times:
            ad[f].append((c, t))
        
        while mheap:
            node = heapq.heappop(mheap)
            
            if node in visited:
                continue
            else:
                visited.add(node)
            
            for nei in ad[node[1]]:
                c_dist = dist[node[1]] + nei[0]
                if c_dist < dist[nei[1]]:
                    dist[nei[1]] = c_dist
                    heapq.heappush(mheap, (c_dist, nei[1]))
        
        if float('inf') in dist.values():
            return -1
        else:
            return max(dist.values())
            
            
        
        
        
        