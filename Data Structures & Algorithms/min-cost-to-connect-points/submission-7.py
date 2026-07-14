class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                cost = abs(x1 - x2) + abs(y1 - y2)
                edges.append((cost, i, j))

        edges.sort()

        parents = [i for i in range(len(points))]
        ranks = [0 for _ in range(len(points))]

        def find(parents, i):
            if parents[i] != i:
                parents[i] = find(parents, parents[i])
            return parents[i]

        def union(parents, ranks, i, j):
            irep = find(parents, i)
            jrep = find(parents, j)

            # cycle found
            if irep == jrep:
                return True

            if ranks[irep] > ranks[jrep]:
                parents[jrep] = irep
            elif ranks[irep] < ranks[jrep]:
                parents[irep] = jrep
            else:
                parents[jrep] = irep
                ranks[irep] += 1

            return False

        total = 0
        edge = 0
        for cost, i, j in edges:
            if not union(parents, ranks, i, j):
                total += cost
                edge += 1
            if edge == n - 1:
                break

        return total

            
