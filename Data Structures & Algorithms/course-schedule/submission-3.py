class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)]

        def dfs(curr):
            if visited[curr] == 1:
                return False
            if visited[curr] == 2:
                return True

            visited[curr] = 1

            for course, prerequisite in prerequisites:
                if prerequisite == curr:
                    if not dfs(course):
                        return False

            visited[curr] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True