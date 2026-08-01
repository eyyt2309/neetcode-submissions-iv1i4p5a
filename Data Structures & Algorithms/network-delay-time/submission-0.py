import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s - 1].append((t, d - 1))

        dist = [float('inf') for _ in range(n)]
        dist[k - 1] = 0
        heap = []

        heapq.heappush(heap, (k - 1, 0))
        
        while heap:
            source, current_time = heapq.heappop(heap)
            if current_time > dist[source]:
                continue
            for distance, nei in adj[source]:
                if current_time + distance < dist[nei]:
                    dist[nei] = current_time + distance
                    heapq.heappush(heap, (nei, current_time + distance))

        if float('inf') in dist:
            return -1
        else:
            return max(dist)
        