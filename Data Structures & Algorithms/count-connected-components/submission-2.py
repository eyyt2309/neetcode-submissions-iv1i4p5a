class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parents = list(range(n))
        ranks = [0 for _ in range(n)]

        for u, v in edges:
            self.union(parents, ranks, u, v)

        components = set()

        for i in range(n):
            components.add(self.find(parents, i))

        return len(components)
    
    def find(self, parents, i):
        if parents[i] == i:
            return i
        
        return self.find(parents, parents[i])

    def union(self, parents, ranks, i, j):

        irep = self.find(parents, i)
        jrep = self.find(parents, j)

        if irep == jrep:
            return True

        if ranks[irep] < ranks[jrep]:
            parents[irep] = jrep
        elif ranks[irep] > ranks[jrep]:
            parents[jrep] = irep
        else:
            parents[irep] = jrep
            ranks[jrep] += 1

