from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            s, turns = queue.popleft()

            if s == target:
                return turns

            for pos in range(4):
                old_num = int(s[pos])

                add_num = (old_num + 1) % 10
                minus_num = (old_num - 1) % 10

                turn_up = s[:pos] + str(add_num) + s[pos + 1:]
                turn_down = s[:pos] + str(minus_num) + s[pos + 1:]

                for new_state in [turn_up, turn_down]:
                    if (
                        new_state not in deadends
                        and new_state not in visited
                    ):
                        visited.add(new_state)
                        queue.append((new_state, turns + 1))

        return -1