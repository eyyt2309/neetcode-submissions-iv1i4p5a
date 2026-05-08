from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prerequisite_set = set(tuple(x) for x in prerequisites)
        visited = [0 for _ in range(numCourses)]
        stack = deque()

        for course, visit in enumerate(visited):
            if not self.topoSort(course, prerequisite_set, visited, stack):
                return []

        topo = []

        while stack:
            topo.append(stack.pop())
        return topo

    def topoSort(self, course, prerequisite_set, visited, stack):
        if visited[course] == 1:
            return False
        elif visited[course] == 2:
            return True
        
        visited[course] = 1

        for crse, prerequisite in prerequisite_set:
            if course == prerequisite:
                if not self.topoSort(crse, prerequisite_set, visited, stack):
                    return []

        visited[course] = 2
        stack.append(course)
        return True



