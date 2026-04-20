class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        n = len(s) - 1

        while(i < n):
            if ((ord(s[i]) >= 48 and ord(s[i]) <= 57) or (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) ):
                if ((ord(s[n]) >= 48 and ord(s[n]) <= 57) or (ord(s[n]) >= 65 and ord(s[n]) <= 90) or (ord(s[n]) >= 97 and ord(s[n]) <= 122) ):
                    print(s[i], s[n])
                    if (s[i] == s[n]):
                        i += 1
                        n -= 1
                        continue
                    else:
                        return False
                else:
                    n -= 1
                    continue
            else:
                i += 1
                continue

        return True