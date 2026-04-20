class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            print(i, stack)
            if not stack:
                stack.append((i, heights[i]))   # 0 is index, 1 is value
                continue
            
            

            if heights[i] < stack[-1][1]: # Breaks the extension, pop the bigger elements.
                pop_count = 0
                while (stack and heights[i] < stack[-1][1]):
                    popped_height = stack.pop()
                    area = (i - popped_height[0]) * popped_height[1]
                    max_area = max(max_area, area)
                    print(f'{stack}, max area: {max_area}')
                    pop_count += 1
                    stack.append((i - pop_count, heights[i]))
                    print(stack)
            else:
                if (stack[-1][1] != heights[i]):
                    stack.append((i, heights[i]))

        print("i", i)
        while(stack):
            popped_height = stack.pop()
            area = (i - popped_height[0] + 1) * popped_height[1]
            max_area = max(max_area, area)
            print(f'{stack}, max area: {max_area}')
            
        return max_area


                    

        print(stack)