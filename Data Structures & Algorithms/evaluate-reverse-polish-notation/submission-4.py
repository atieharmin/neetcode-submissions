class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(a, b, exp):
            if exp == "+":
                return a + b
            if exp == "*":
                return a * b
            if exp == "/":
                return a / b
            if exp == "-":
                return a - b
        def is_exp(exp):
            if exp in ["+", "-", "/", "*"]:
                return True
            else:
                return False

        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in range(len(tokens)-1,-1,-1):
            stack.append(tokens[i])

        sec_stack = []
        while len(stack) > 0:
            a = stack.pop()
            if is_exp(a):
                b = sec_stack.pop()
                c = sec_stack.pop()
                res = int(evaluate(int(c), int(b), a))
                stack.append(res)
            else:
                sec_stack.append(a)

        return sec_stack.pop()