class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(parents, i):
            if parents[i] == i:
                return i
            return find(parents, parents[i])
        def union(parents, rank, i, j):
            irep = find(parents, i)
            jrep = find(parents, j)

            if irep == jrep:
                return True

            if rank[irep] < rank[jrep]:
                parents[irep] = jrep
            elif rank[irep] > rank[jrep]:
                parents[jrep] = irep
            else:
                parents[irep] = jrep
                rank[jrep] += 1

        parents = list(range(n))
        rank = [0 for _ in range(n)]

        for edge in edges:
            if union(parents, rank, edge[0], edge[1]):
                return False
        connected = True
        for i in range(n):
            for j in range(i, n):
                if find(parents, i) != find(parents, j):
                    connected = False

        return connected