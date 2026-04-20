class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        max_val = -1


        for i in nums:
            
            if dic[i - 1]:
                if dic[i]:
                    dic[i] += dic[i - 1] + 1
                else:
                    dic[i] = dic[i - 1]
            
            
            if dic[i]:
                dic[i] += 1
            else:
                dic[i] = 1
            max_val = max(max_val, dic[i])

        print(dic)
        