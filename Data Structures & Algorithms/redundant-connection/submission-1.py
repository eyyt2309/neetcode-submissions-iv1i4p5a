class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        for u, v in edges:
            if self.find(parents, u) == self.find(parents, v):
                return [u,v]
            self.unionSet(parents, u, v, rank)


    def find(self, parents, i):
        # if a node is not the parent of itself, find its parent
        if parents[i] != i:
            parents[i] = self.find(parents, parents[i])
        return parents[i]

    def unionSet(self, parents, i , j, rank):

        irep = self.find(parents, i)

        jrep = self.find(parents, j)

        if irep == jrep:
            return

        if rank[irep] < rank[jrep]:
            parents[irep] = jrep
        elif rank[irep] > rank[jrep]:
            parents[jrep] = irep
        elif rank[irep] == rank[jrep]:
            parents[irep] = jrep
            rank[jrep] += 1