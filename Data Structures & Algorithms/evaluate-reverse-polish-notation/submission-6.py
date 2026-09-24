class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            right = eval()
            left = eval()

            if token == "+":
                return left + right
            elif token == "-":
                return left - right
            elif token == "/":
                return int(left / right)
            elif token == "*":
                return left * right
        
        return eval()