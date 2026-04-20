class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count_list = [0] * 26   # Using it as a dict.
        max_window_len = -1
        max_freq_char_count = -1
        # window len - count(max_freq_char_in_the_window) = k
        while (l <= r and r < len(s)):
            count_list[ord(s[r]) - ord('A')] += 1
            
            max_freq_char_count = max(max_freq_char_count, count_list[ord(s[r]) - ord('A')])
            print(s[l:r+1])
            print("Max freq char count: ", max_freq_char_count)
            if (((r - l + 1) - max_freq_char_count) == k):
                print("window found with len: ", r - l + 1)
                max_window_len = max(max_window_len, r - l + 1)
            elif (((r - l + 1) - max_freq_char_count) > k):
                print("Decrementing by 1: ", count_list[ord(s[l]) - ord('A')])
                count_list[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        
        print(s[l:r+1])
        print(count_list)
        return len(s) if max_window_len == -1 else max_window_len
