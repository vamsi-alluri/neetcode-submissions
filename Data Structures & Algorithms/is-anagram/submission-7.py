class Solution:
    def add_to_dic(self, ref_dic: dict, string:str):
        for i in string:
            if i in ref_dic:
                ref_dic[i] += 1
            else:
                ref_dic[i] = 1

    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        self.add_to_dic(s_dic, s)

        flag = False
        for i in t:
            if i in s_dic:
                s_dic[i] -= 1
                flag = True
                if (s_dic[i] == 0):
                    flag = False
            else:
                return False
        
        return True if flag == False else False