from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = deque()

        length = len(position)

        arr = []

        for idx in range(length):
            arr.append((position[idx], speed[idx]))

        sorted_arr = sorted(arr, key= lambda x: x[0])

        for idx in range(length - 1, -1 , -1):
            time_taken = (target - sorted_arr[idx][0]) / sorted_arr[idx][1]
            if idx == length - 1:
                stack.append(time_taken)
            # if time_taken <= slowest car currently, join fleet and continue
            elif time_taken <= stack[-1]:
                continue
            # if time_taken > slowest car, make new fleet and append to stack
            elif time_taken > stack[-1]:
                stack.append(time_taken)

        return len(stack)