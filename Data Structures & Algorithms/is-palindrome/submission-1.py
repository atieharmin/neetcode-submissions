import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub(r"[^a-zA-Z0-9]","",s)
        inv = s[::-1]
        # for i,t in zip(s,inv):
        #     if i == t:
        #         continue
        #     else:
        #         return False
        # return True
        if inv == s:
            return True
        else:
            return False