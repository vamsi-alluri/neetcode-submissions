class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            print(nums[i], target, diff)

            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[diff] = i
        print(dic)
        return []