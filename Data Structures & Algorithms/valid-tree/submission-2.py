class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        def find(parents, i):
            if parents[i] != i:
                parents[i] = find(parents, parents[i])
            return parents[i]
        def union(parents, ranks, i, j):
            irep = find(parents, i)
            jrep = find(parents, j)

            if irep == jrep:
                return True

            if ranks[irep] > ranks[jrep]:
                parents[jrep] = irep
            elif ranks[irep] < ranks[jrep]:
                parents[irep] = jrep
            else:
                parents[jrep] = irep
                ranks[irep] += 1
        num_edges = len(edges)
        for i, j in edges:

            if union(parents, ranks, i, j):
                return False
        return True and num_edges == n-1