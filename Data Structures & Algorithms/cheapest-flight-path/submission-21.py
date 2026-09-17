from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = defaultdict(set)
        heap = []
        prices = [
            [float('inf')] * (k + 2)
            for _ in range(n)
        ]
        # create dict of sets for faster lookup
        for source, dest, price in flights:
            flight_dict[source].add((dest, price))


        heapq.heappush(heap, (0, 0, src)) # (price, stops, dest)

        while heap:
            curr_price, flights_taken, source = heapq.heappop(heap)
            # outdated state
            if curr_price > prices[source][flights_taken]:
                continue

            # cheapest valid way to dst
            if source == dst:
                return curr_price

            # already used max number of flights
            if flights_taken == k + 1:
                continue

            for dest, price in flight_dict[source]:
                new_price = curr_price + price
                new_flights = flights_taken + 1

                if new_price < prices[dest][new_flights]:
                    prices[dest][new_flights] = new_price

                    heapq.heappush(
                        heap,
                        (new_price, new_flights, dest)
                    )

        return -1


        