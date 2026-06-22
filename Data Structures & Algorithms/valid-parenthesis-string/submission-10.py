from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        p_stack = deque()
        s_stack = deque()

        for i, ch in enumerate(s):
            if ch == "(":
                p_stack.append(i)
            elif ch == "*":
                s_stack.append(i)
            elif ch == ")":
                if p_stack:
                    p_stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False

        while p_stack and s_stack:
            if p_stack.pop() > s_stack.pop():
                return False

        if p_stack:
            return False
        else:
            return True
