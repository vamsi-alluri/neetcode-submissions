class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_set = []
        substrings = []
        substring = ""
        for i in s:
            if (i in visited_set):
                substrings.append(substring)
                substring = ""
                visited_set = []
                continue
            
            substring += i
            visited_set.append(i)
        substrings.append(substring)
        print(substrings)
        return len(max(substrings, key=len))