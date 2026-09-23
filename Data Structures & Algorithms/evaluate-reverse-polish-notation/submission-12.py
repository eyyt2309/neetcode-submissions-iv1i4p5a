from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                c = int(a / b)
                stack.append(c)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            else:
                stack.append(int(token))
        return stack.pop()                