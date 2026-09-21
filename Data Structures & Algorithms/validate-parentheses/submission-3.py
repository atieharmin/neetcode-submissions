class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = defaultdict(str)
        dic['('], dic['['], dic['{'] = ')' , ']', '}'
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            t = stack.pop()
            if dic[t] == s[i]:
                continue
            else:
                stack.append(t)
                stack.append(s[i])
        
        if len(stack) == 0:
            return True
        return False