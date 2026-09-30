from heapq import heappush, heappop

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        busy = []  # (endTime, room)
        count = [0] * n

        meetings.sort()

        for start, end in meetings:
            duration = end - start

            # Free every room available by this meeting's start
            while busy and busy[0][0] <= start:
                endTime, room = heappop(busy)
                heappush(available, room)

            if available:
                # Lowest numbered room
                room = heappop(available)

                heappush(busy, (end, room))

            else:
                # No rooms available:
                # wait for earliest room to become free
                endTime, room = heappop(busy)

                heappush(
                    busy,
                    (endTime + duration, room)
                )

            count[room] += 1

        return max(range(n), key=lambda room: count[room])