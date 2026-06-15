class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
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

            if ranks[irep] < ranks[jrep]:
                parents[irep] = jrep
            elif ranks[irep] > ranks[jrep]:
                parents[jrep] = irep
            else:
                parents[irep] = jrep
                ranks[jrep] += 1

        for i, j in edges:
            union(parents, ranks, i, j)

        components = set()
        for node in parents:
            print(node)
            components.add(find(parents, node))

        return len(components)
