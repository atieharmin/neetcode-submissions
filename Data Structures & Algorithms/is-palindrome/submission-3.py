class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub(r"[^a-zA-Z0-9]","",s)
        # if s[::-1] == s:
        #     return True
        # else:
        #     return False
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        return True