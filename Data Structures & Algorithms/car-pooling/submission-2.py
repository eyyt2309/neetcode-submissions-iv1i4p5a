import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        trip_idx = 0
        heap = []
        curr_passengers = 0

        last_end = trips[-1][2]

        for time in range(last_end + 1):
            while trip_idx < len(trips) and time == trips[trip_idx][1]:
                passengers, start, end = trips[trip_idx]
                heapq.heappush(heap, (end, passengers, start))
                trip_idx += 1
                curr_passengers += passengers
            while heap and heap[0][0] == time:
                _, passengers, _ = heapq.heappop(heap)
                curr_passengers -= passengers

            if curr_passengers > capacity:
                return False

        return True
 