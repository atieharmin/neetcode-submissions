class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        final = []
        for value in strs:
            s = "".join(sorted(value))
            l = dic.get(s)
            if l == None:
                dic[s] = [value]
            else:
                l.append(value)
        final = [dic[i] for i in dic]
        return final