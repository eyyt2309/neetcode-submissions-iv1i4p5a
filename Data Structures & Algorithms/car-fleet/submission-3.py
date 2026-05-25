from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []

        for i in range(len(position)):
            arr.append([position[i],speed[i]])

        arr.sort(key=lambda x: x[0], reverse=True)
        print(arr)

        stack = deque()
        prev_time_taken = 0
        for car in arr:
            if not stack:
                prev_time_taken = (target - car[0]) / car[1]
                stack.append(car)
            else:
                time_taken = (target - car[0]) / car[1]
                if time_taken > prev_time_taken:
                    prev_time_taken = time_taken
                    stack.append(car)

        return len(stack)
