class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges))]
        ranks = [0 for _ in range(len(edges))]

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
            elif ranks[irep] == ranks[jrep]:
                parents[jrep] = irep
                ranks[irep] += 1

            return False

        print(edges)
        
        for i, j in edges:
            if union(parents, ranks, i - 1, j - 1):
                last = [i,j]

        return last