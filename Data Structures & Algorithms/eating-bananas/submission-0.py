class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        max_p = max(piles)
        min_p = 1

        piles.sort()

        while min_p <= max_p:
            mid = (min_p + max_p) // 2
            time = 0

            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)

            if time <= h:
                res = min(mid, res)
                max_p = mid - 1
            else:
                min_p = mid + 1
        
        return res