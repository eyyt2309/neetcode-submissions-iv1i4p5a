from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        divisions = defaultdict(set)
        ans = []

        for i in range(len(equations)):
            divisions[equations[i][0]].add((equations[i][1], values[i]))
            divisions[equations[i][1]].add((equations[i][0], (1 / values[i])))

        for q1, q2 in queries:
            if q1 not in divisions or q2 not in divisions:
                ans.append(-1)
                continue
            visited = set()
            visited.add(q1)
            queue = deque([(q1, 1)])

            found = False
            while queue:
                curr, curr_product = queue.popleft()
                if curr == q2:
                    found = True
                    ans.append(curr_product)
                    break
                for neighbor, product in divisions[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_product * product))

            if not found:
                ans.append(-1)
        
        return ans