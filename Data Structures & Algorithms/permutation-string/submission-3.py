class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l, r = 0, len(s1) - 1

        while (r < len(s2)):
            print(sorted(s2[l:r+1]), r)
            if (sorted(s2[l:r+1]) != sorted(s1)):
                r += 1
                l += 1
            else:
                return True
        return False