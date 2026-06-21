from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        print(freq)

        heapq.heapify(hand)

        while hand:
            minval = heapq.heappop(hand)
            if freq[minval] == 0:
                continue

            freq[minval] -= 1
            for i in range(minval + 1, minval + groupSize):
                if freq[i] == 0:
                    return False
                freq[i] -= 1

        return True