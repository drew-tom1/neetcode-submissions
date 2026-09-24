class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = set()
        ad = defaultdict(list)
        costs = defaultdict(lambda: float('inf'))
        costs[(src, 0)] = 0
        mheap = []
        res = float('inf')
        heapq.heappush(mheap, (0, src, 0))

        for f, t, c in flights:
            ad[f].append((c,t))

        while mheap:
            cost, node, hops = heapq.heappop(mheap)

            for nei in ad[node]:
                candidate_cost = costs[(node, hops)] + nei[0]

                if candidate_cost < costs[(nei[1], hops + 1)] and hops <= k:
                    costs[(nei[1], hops + 1)] = candidate_cost
                    heapq.heappush(mheap, (costs[(nei[1], hops + 1)], nei[1], hops + 1))

        for i in range(k + 2):
            res = min(res, costs[(dst, i)])
        
        if res == float('inf'):
            return -1
        else:
            return res
        