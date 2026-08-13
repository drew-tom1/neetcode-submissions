class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ad = defaultdict(list)
        in_degree = [0] * numCourses

        for c, p in prerequisites:
            ad[p].append(c)
            in_degree[c] += 1
        
        queue = deque([c for c in range(len(in_degree)) if in_degree[c] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in ad[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
            
        if len(order) == numCourses:
            return order
        
        return []
        

        