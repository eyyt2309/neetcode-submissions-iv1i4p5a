from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = deque()

        for part in parts:
            if part == '..':
                print(stack)
                if stack:
                    stack.pop()
            elif part != '' and part != '.':
                stack.append(part)

        return "/" + "/".join(stack)


