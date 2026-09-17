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
            j = i+1
            while s[j] != "#":
                j += 1
            length = int(s[i+1:j])
            word = s[j+1:j+length+1]
            final.append(word)
            i = j+length+1
        return final
