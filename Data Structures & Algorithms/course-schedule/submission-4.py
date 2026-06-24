class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for course, prerequisite in prerequisites:
            if course not in courses:
                courses[course] = [prerequisite]
            else:
                courses[course].append(prerequisite)

        arr = [0 for _ in range(numCourses)]

        def dfs(course):
            if arr[course] == 1:
                return False
            arr[course] = 1
            if course in courses:
                for prerequisite in courses[course]:
                    if not dfs(prerequisite):
                        return False
            
            arr[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

