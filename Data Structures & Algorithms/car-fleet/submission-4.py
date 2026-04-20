class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        def time(p, s):
            return (target - p) / s

        carsN = len(position)
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(key=lambda x: x[0], reverse=True)

        stack = []
        stack.append(time(pairs[0][0], pairs[0][1]))
        for p, s in pairs[1:]:
            
            eta = time(p, s)
            if eta > stack[-1]:
                stack.append(eta)

        return len(stack)


