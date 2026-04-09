from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for ch in s:
            match ch:
                case "[":
                    stack.append(ch)
                case "(":
                    stack.append(ch)
                case "{":
                    stack.append(ch)
                case "]":
                    if stack and stack[-1] == "[" :
                        stack.pop()
                    else:
                        return False
                case ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                case "}":
                    if stack and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        else:
            return True

        