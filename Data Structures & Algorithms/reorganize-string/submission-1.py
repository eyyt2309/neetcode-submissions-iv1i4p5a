from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        ch_count = Counter(s)
        heap = []
        ans = ""

        for char in ch_count:
            heapq.heappush(heap, (-ch_count[char], char))

        while heap:
            if not ans:
                count, char = heapq.heappop(heap)
                ans+=char
                if count + 1 < 0:
                    heapq.heappush(heap, (count + 1, char))                
            elif heap and ans[-1] != heap[0][1]:
                count, char = heapq.heappop(heap)
                ans+=char
                if count + 1 < 0:
                    heapq.heappush(heap, (count + 1, char))
            elif len(heap) >= 2:
                temp_count, temp_char = heapq.heappop(heap)
                count, char = heapq.heappop(heap)
                ans+=char
                if count + 1 < 0:
                    heapq.heappush(heap, (count + 1, char))
                heapq.heappush(heap, (temp_count, temp_char))
            else:
                return ""

        return ans if len(ans) == len(s) else ""


