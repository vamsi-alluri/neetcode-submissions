class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max_height = [height[0]]
        suffix_max_height = [height[-1]]
        water_trapped = 0

        for i in range(1, n):
            prefix_max_height.append(max(prefix_max_height[-1], height[i]))
            suffix_max_height.append(max(suffix_max_height[-1], height[n - 1 - i]))
        suffix_max_height = suffix_max_height[::-1]

        for i in range(n):
            water_trapped += (min(prefix_max_height[i], suffix_max_height[i]) - height[i])
        return water_trapped

