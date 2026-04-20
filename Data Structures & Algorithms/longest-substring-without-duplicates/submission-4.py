class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        substrings = []
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            substrings.append(s[l:r+1])
            res = max(res, r - l + 1)
        print(substrings)
        return res