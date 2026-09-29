class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for t in temperatures]
        stack1 = []
        stack2 = []
        for i in range(len(temperatures)-1,-1,-1):
            stack1.append((temperatures[i],i))


        while len(stack1) != 0:
            a = stack1.pop()
            if len(stack2) > 0:
                b = stack2.pop()
            else:
                stack2.append(a)
                continue
            if a[0] > b[0]:
                i = b[1]
                j = a[1]
                res[i] = j - i
                stack1.append(a)
                continue
            elif b[0] >= a[0]:
                stack2.append(b)
            stack2.append(a)
                    
        return res
