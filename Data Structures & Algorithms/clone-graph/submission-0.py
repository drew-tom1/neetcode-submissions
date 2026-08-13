"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        clone = defaultdict(lambda: Node(0))

        def dfs(n):
            # if copy node exists, return early
            if n in clone:
                return clone[n]

            # defaultdict initializes empty nodes, fill in value
            clone[n].val = n.val
            # for each neighbor, we append that cloned node
            for nei in n.neighbors:
                clone[n].neighbors.append(dfs(nei))

            return clone[n]

        return dfs(node)
                


