class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req_map = defaultdict(list)
        checked = set()

        for c, p in prerequisites:
            req_map[p].append(c)

        def dfs(crs):
            if crs in checked:
                return False
            if req_map[crs] == []:
                return True

            checked.add(crs)
            
            for neighbor in req_map[crs]:
                if not dfs(neighbor):
                    return False
            
            checked.remove(crs)
            req_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
