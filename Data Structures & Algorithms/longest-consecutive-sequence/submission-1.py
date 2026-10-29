class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set:
                local_longest_seq = 0
                curr_num = num + 1
                while curr_num - 1 in nums_set:
                    curr_num += 1
                    local_longest_seq += 1
                longest_seq = max(longest_seq, local_longest_seq)
        return longest_seq
