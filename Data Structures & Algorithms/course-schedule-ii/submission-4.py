from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [0 for _ in range(numCourses)]
        self.cycle = False
        self.result = deque()

        def dfs(course):
            self.visited[course] = 1

            for rq in prerequisites:
                if course == rq[1] and self.visited[rq[0]] == 0:
                    dfs(rq[0])
                elif course == rq[1] and self.visited[rq[0]] == 1:
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

        ans = []
        while self.result:
            ans.append(self.result.pop())

        return ans