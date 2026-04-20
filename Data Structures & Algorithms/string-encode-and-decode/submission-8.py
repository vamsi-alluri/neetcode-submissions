import base64
class Solution:

    def encode(self, strs):
        return ''.join(f"{len(base64.b64encode(s.encode()).decode())}:{base64.b64encode(s.encode()).decode()}" for s in strs)

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(base64.b64decode(s[j:j+length]).decode())
            i = j + length
        return res

