from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [0 for _ in range(numCourses)]
        self.cycle = False
        self.result = deque()
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course):
            self.visited[course] = 1

            for prereq in graph[course]:
                if self.visited[prereq] == 0:
                    dfs(prereq)
                elif self.visited[prereq] == 1:
                    self.cycle = True
                    break
                else:
                    continue

            self.visited[course] = 2
            self.result.append(course)

        for course in range(numCourses):
            if self.visited[course] == 0:
                dfs(course)

        if self.cycle == True:
            return []
        return list(self.result)