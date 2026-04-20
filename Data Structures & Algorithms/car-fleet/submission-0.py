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
        
        count = 0
        for i in range(0,len(time)-1):
            if time[i]<time[i+1]:
                count += 1
        
        dict_time = {}
        for i in time:
            if i in dict_time:
                dict_time[i] += 1
            else:
                dict_time[i] = 1

        return len(dict_time)-count


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


