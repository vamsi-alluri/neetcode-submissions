class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {}

        for i in nums:  # n
            if i not in freq_dic:
                freq_dic[i] = 1
            else:
                freq_dic[i] += 1
        print(freq_dic)

        nums = []
        while(k > 0):  # k
            max_ =  -1
            max_k = -1
            for k_, v in freq_dic.items():   # len(set(n))    
                if (max_ < v):
                    max_k = k_
                    max_ = v
            nums.append(max_k)
            freq_dic[max_k] = 0
            k -= 1
        return nums


        
            
        