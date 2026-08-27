from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        heap = []

        for char in char_count:
            heapq.heappush(heap, (-char_count[char], char))
        
        arr = []
        while heap:
            if not arr or arr[-1] != heap[0][1]:
                count, char = heapq.heappop(heap)
                arr.append(char)
                count += 1
                if count != 0:
                    heapq.heappush(heap,(count, char))
            elif arr[-1] == heap[0][1]: # same char as current top of heap
                remove_count, remove_char = heapq.heappop(heap) # remove top of heap temporarily

                if heap:
                    count, char = heapq.heappop(heap) # pop next element
                else:
                    return "" # no next element return ""
                arr.append(char)
                count += 1
                if count != 0:
                    heapq.heappush(heap,(count, char))

                heapq.heappush(heap, (remove_count, remove_char)) # repush top of heap

        return "".join(arr)