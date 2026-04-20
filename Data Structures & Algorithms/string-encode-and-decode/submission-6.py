import base64
class Solution:

    def encode(self, strs):
        return '|'.join(base64.b64encode(s.encode()).decode() for s in strs)

    def decode(self, s):
        if not s:
            return []
        return [base64.b64decode(part).decode() for part in s.split('|')]

