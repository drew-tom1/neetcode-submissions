class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0

        stack = []

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for p, s in cars:
            print(p, s)
            ttd = (target - p) / s # time to destination

            if not stack: # edge case, if stack is empty
                res += 1
                stack.append(ttd)

            if ttd > stack[-1]: # 
                res += 1
                stack.append(ttd)
        
        
        return res

        

        