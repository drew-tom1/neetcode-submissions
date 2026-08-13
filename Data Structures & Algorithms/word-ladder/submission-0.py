class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        queue = deque([])
        queue.append(beginWord)
        graph = defaultdict(list)
        visited = set()

        # create graph
        for i in range(len(wordList)):
            word = list(wordList[i])
            for j in range(len(word)):
                temp = word[j]
                word[j] = "*"
                graph[''.join(word)].append(wordList[i])
                word[j] = temp
        
        while queue:
            ql = len(queue)

            for _ in range(ql):
                node = queue.popleft()

                for i in range(len(node)):
                    word = list(node)
                    temp = word[i]
                    word[i] = "*"
                    lookup = ''.join(word)

                    for nei in graph[lookup]:
                        if nei == endWord:
                            return res + 2
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)  
            res += 1
        
        return 0
                    
                

                

