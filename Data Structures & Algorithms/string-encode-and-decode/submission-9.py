import base64
class Solution:

    def encode(self, strs):
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        res, i = 0, 0
        result = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            result.append(s[j:j+length])
            i = j + length
        return result

