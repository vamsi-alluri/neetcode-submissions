class Solution:

    def encode(self, strs: List[str]) -> str:
        print(chr(126).join(strs))
        
        return chr(126).join(strs)

    def decode(self, s: str) -> List[str]:

        if (not s):
            return []
        print(s)
        return s.split(chr(126))
