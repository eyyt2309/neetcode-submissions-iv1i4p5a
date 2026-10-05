from heapq import heappush, heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0: 
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c > 0:
            heappush(heap, (-c, 'c'))

        s = ""

        while heap:
            if len(s) <= 1:
                freq, ch = heappop(heap)
                s += ch
                if freq + 1 < 0:
                    heappush(heap, (freq + 1, ch))
            else:
                if len(s) >= 2 and s[-1] == s[-2] and heap[0][1] == s[-1]:
                    tempFreq, tempCh = heappop(heap)
                    if heap:
                        freq, ch = heappop(heap)
                        s += ch

                        if freq + 1 < 0:
                            heappush(heap, (freq + 1, ch))
                    else:
                        break
                    heappush(heap, (tempFreq, tempCh))
                else:
                    freq, ch = heappop(heap)
                    s += ch

                    if freq + 1 < 0:
                        heappush(heap, (freq + 1, ch))


        return s    



                
