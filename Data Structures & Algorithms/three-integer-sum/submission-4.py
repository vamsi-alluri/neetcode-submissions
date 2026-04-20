class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers) - 1
        while(i < n):
            _sum = numbers[i] + numbers[n]
            if _sum < target:
                i += 1
            elif (_sum > target):
                n -= 1
            else:
                return [numbers[i], numbers[n]]
        return []

    def is_list_in_list_of_lists(self, l, ll) -> bool:
        for cur_list in ll:  # Iterate through existing results.
            print("Checking lists ", l, cur_list)
            if (l == cur_list):
                print("Equal.")
                return True
        return False
            # while (while_itr < l):
            #     # [0,0,0] [1,2,3]
            #     # [0,0,0] [0,0,0]
            #     if (two_sum_res[while_itr] != j[while_itr]):
            #         break
            #     else:
            #         w_while_itritr += 1
            # if (while_itr == l - 1):
            #     continue
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # n * log n
        
        _res = []
        for i in range(len(nums)): # n
            two_sum_res = self.twoSum(nums[i+1:], -nums[i]) # n
            if (two_sum_res != []):
                two_sum_res.append(nums[i])
                if (_res == []):  # First result.
                    _res.append(two_sum_res)

                if (self.is_list_in_list_of_lists(two_sum_res, _res) == False):
                    _res.append(two_sum_res)
                        
            
        return _res

        