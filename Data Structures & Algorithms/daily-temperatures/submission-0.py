class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        print(res)

        stack = []

        for day_itr in range(len(temperatures)):
            print(f"Stack: {stack}")
            while (stack and temperatures[day_itr] > temperatures[stack[-1]]):
                day_idx = stack.pop()
                idx_difference = day_itr - day_idx
                print(idx_difference)
                res[day_idx] = idx_difference 

            stack.append(day_itr)
        
        return res