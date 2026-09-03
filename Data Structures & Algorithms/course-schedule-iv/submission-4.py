from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # check whether course ui is a course of vj
        pq = defaultdict(set)

        # cache[prereq] = [course1, course2 ...]

        for p, q in prerequisites:
            pq[p].add(q)

        cache = {}
        
        def dfs(prerequisite):
            if prerequisite in cache:
                return cache[prerequisite]

            reachable = set()

            for nextCourse in pq[prerequisite]:
                reachable.add(nextCourse)
                reachable.update(dfs(nextCourse))

            cache[prerequisite] = reachable
            return reachable

        ans = []

        for prerequisite in range(numCourses):
            dfs(prerequisite)

        for p, q in queries:
            if q in cache[p]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            
