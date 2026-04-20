class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position,speed))
        pair.sort(key=lambda x:x[0])
        sorted_position,sorted_speed = zip(*pair)
        sorted_position = list(sorted_position)
        sorted_speed = list(sorted_speed)

        time = []
        for i in range(0,len(position)):
            time.append((target - sorted_position[i])/sorted_speed[i])
        
        ans = 0
        stack = time[::-1]
        for i in range(len(stack)-1):
            if stack[i] <= stack[i+1]:
                ans += 1
            else:
                continue
        
        return ans


# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
#         carsN = len(position)

#         hrs = []


#         for i in range(carsN):
#             hrs.append(round((target - position[i]) / speed[i]))

#         for i in sorted(enumerate(zip(position, hrs))):
#         print(position)
#         print(speed)
#         print(hrs)

#         return 0


