class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return " "
        s = ""
        for i in range(len(strs)):
            s += "#" + str(len(strs[i])) + "#" + strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        if s == " ":
            return []
        final = []
        i = 0
        while i < len(s):
            if(s[i] == "#"):
                l = ""
                for j in range(i+1,len(s)):
                    if(s[j] == "#"):
                        break
                    l += s[j]
                length = int(l)
            word = ""
            for k in range(j+1,j+length+1):
                word+=s[k]
            final.append(word)
            i = j+length+1
        return final
