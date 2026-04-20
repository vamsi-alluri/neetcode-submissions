class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for i in strs:
            res_s = []
            for j in strs:
                if sorted(i) == sorted(j):
                    res_s.append(j)
            if (res_s not in res):
                res.append(res_s)
        return res
