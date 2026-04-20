class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = set()
        for i in s1:
            s1_set.add(i)
        print("s1_set", s1_set)

        window_size = len(s1)
        l, r = 0, window_size - 1

        while (r < len(s2)):
            print(s2[l:r+1], r)
            if (set(s2[l:r+1]) != s1_set):
                r += 1
                l += 1
            else:
                return True
        return False