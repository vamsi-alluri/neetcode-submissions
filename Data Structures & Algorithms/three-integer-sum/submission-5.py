class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        i = 0
        n = len(numbers) - 1
        results = []
        while(i < n):
            _sum = numbers[i] + numbers[n]
            if _sum < target:
                i += 1
            elif (_sum > target):
                n -= 1
            else:
                results.append([-target, numbers[i], numbers[n]])
                break
        print(results)
        return results

    def is_two_sum_result_a_duplicate(self, two_sum_results:List[List[int]], three_sum_results:List[List[int]]) -> bool:
        for three_sum_result in three_sum_results:  # Iterate through existing results.
            for two_sum_result in two_sum_results:
                print("Checking lists ", two_sum_result, three_sum_result)
                if (two_sum_result == three_sum_result):
                    print("Equal.")
                    return True
        return False
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # n * log n
        print("Sorted: ", nums)
        
        _res = []
        for i in range(len(nums)): # n
            two_sum_results = self.twoSum(nums[i+1:], -nums[i]) # n
            print("i, Two sum result: ", nums[i], two_sum_results)
            if (two_sum_results != []):
                
                if (_res == []):  # First result.
                    _res.extend(two_sum_results)

                if (self.is_two_sum_result_a_duplicate(two_sum_results, _res) == False):
                    _res.extend(two_sum_results)
                        
            
        return _res

        