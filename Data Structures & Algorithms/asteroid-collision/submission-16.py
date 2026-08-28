from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        """
        Will only collide if asteroid on left is going right and asteroid on right is going left
        stack[-1] > 0 and incoming asteroid < 0

        """

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            elif stack[-1] * asteroid > 0: # same direction, append to stack
                stack.append(asteroid)
            elif stack[-1] < 0 and asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and asteroid < 0:
                    destroyed = False
                    if abs(stack[-1]) == abs(asteroid): # if same size, pop stack and break early
                        stack.pop()
                        destroyed = True
                        break
                    elif abs(stack[-1]) > abs(asteroid): # skip to next asteroid
                        destroyed = True
                        break
                    elif abs(stack[-1]) < abs(asteroid): # remove top of stack
                        stack.pop()
                if not destroyed:
                    stack.append(asteroid)


        return list(stack)
