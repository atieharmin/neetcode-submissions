import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub(r"[^a-zA-Z0-9]","",s)
        inv = ""
        for i in range(len(s)-1,-1,-1):
            inv+=s[i]
        for i,t in zip(s,inv):
            if i == t:
                continue
            else:
                return False
        return True