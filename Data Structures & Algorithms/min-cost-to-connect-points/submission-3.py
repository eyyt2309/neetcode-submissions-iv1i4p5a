class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        parents = list(range(len(points)))
        ranks = [1 for _ in range(len(points))]

        # generate adjacency matrix
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, weight))
        

        edges.sort(key=lambda x: x[2])

        cost = 0
        count = 0
        for x, y, weight in edges:
            if self.find(parents, x) != self.find(parents, y):
                self.union(parents, ranks, x, y)
                cost += weight
                count += 1
                if count == len(points) - 1:
                    break
        return cost


    def find(self, parents, i):
        if parents[i] != i:
            parents[i] = self.find(parents, parents[i])
        return parents[i]

    def union(self, parents, ranks, i, j):
        irep = self.find(parents, i)
        jrep = self.find(parents, j)

        if irep == jrep:
            return

        if ranks[irep] < ranks[jrep]:
            parents[irep] = jrep
        elif ranks[irep] > ranks[jrep]:
            parents[jrep] = irep
        else:
            parents[irep] = jrep
            ranks[jrep] += 1



            