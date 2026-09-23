from collections import Counter, deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        skip_radiant, skip_dire = 0, 0

        queue = deque(senate)

        while queue and len(Counter(queue)) > 1:
            length = len(queue)
            for _ in range(length):
                senator = queue.popleft()
                if senator == 'R':
                    if skip_radiant > 0:
                        skip_radiant -= 1
                        continue # do not push this senator back into queue
                    else:
                        skip_dire += 1
                        queue.append(senator)
                else:
                    if skip_dire > 0:
                        skip_dire -= 1
                        continue
                    else:
                        skip_radiant += 1
                        queue.append(senator)
        
        if queue[0] == 'R':
            return 'Radiant'
        else:
            return 'Dire'