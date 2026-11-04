class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if not self.right or num <= self.right[0]:
            heapq.heappush_max(self.left, num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) - len(self.right) > 1:
            heapq.heappush(self.right, heapq.heappop_max(self.left))
        elif len(self.right) - len(self.left) > 1:
            heapq.heappush_max(self.left, heapq.heappop(self.right))
        
        
        
    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (self.left[0] + self.right[0]) / 2
        else:
            return self.right[0] if len(self.right) > len(self.left) else self.left[0]

        
        