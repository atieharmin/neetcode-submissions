from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
        # for char in s:
        #     if char in t:
        #         t = t.replace(char, "", 1)
        #         continue
        #     else:
        #         return False
        # return True
        s_counter = Counter (s)
        t_counter = Counter (t)
        if s_counter == t_counter :
            return True
        else:
            return False


