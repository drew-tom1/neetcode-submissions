import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 1
        freq = Counter(tasks)
        task_heap = []
        cooldown = []

        for key in freq.keys():
            heapq.heappush_max(task_heap, (freq[key],key))
        
        while task_heap:
            for _ in range(len(task_heap)):
                task = heapq.heappop_max(task_heap)
                print(task, cooldown)
                if task[0] > 1:
                    heapq.heappush(cooldown,(time + n + 1,task))
                time += 1

                
                if cooldown and cooldown[0][0] == time:
                    available = heapq.heappop(cooldown)[1]
                    heapq.heappush_max(task_heap, (available[0] - 1, available[1]))
                elif not task_heap and cooldown:
                    next_available = heapq.heappop(cooldown)
                    time = next_available[0]
                    next_task = next_available[1]
                    heapq.heappush_max(task_heap, (next_task[0] - 1, next_task[1]))
                    break


        return time - 1
                
        


        
        
        
            

        
        