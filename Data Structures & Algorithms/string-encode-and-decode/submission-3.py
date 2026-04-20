class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:

            print(chr(126).join(strs))
        
            return chr(126).join(strs)
        return ""

    def decode(self, s: str) -> List[str]:

        print(s)
        if (s):
            return s.split(chr(126))
        return []
