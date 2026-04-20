class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prefix_products = [1]
        suffix_products = [1]
        ans = [1]*len_nums
        prev_val = 1

        for i in range(1, len_nums):
            prev_val *= nums[i - 1]
            ans[i] = prev_val
        print(ans)

        temp_ans = [1]*len_nums
        prev_val = 1
        for i in range(len_nums - 2, -1, -1):
            print(i, prev_val, nums[i+1])   
            prev_val *= nums[i + 1]
            ans[i] *= prev_val
            temp_ans[i] = prev_val

        print(temp_ans)
        return ans