class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                r = stack.pop()
                l = stack.pop()
                stack.append(l+r)
            elif token == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(l-r)
            elif token == "*":
                r = stack.pop()
                l = stack.pop()
                stack.append(l*r)
            elif token == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l/r))
            else:
                stack.append(int(token))
        return stack.pop()