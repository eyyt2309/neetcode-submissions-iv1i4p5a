import heapq
from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.maxCount = 0
        self.count = defaultdict(list)
        self.numCount = defaultdict(int)


    def push(self, val: int) -> None:
        currCount = self.numCount.get(val, 0) # get current count of val
        newCount = currCount + 1         
        self.numCount[val] += 1               # increment count of val

        self.maxCount = max(self.maxCount, newCount) # get new maxCount

        self.count[newCount].append(val)

    def pop(self) -> int:
        frequent_last = self.count[self.maxCount].pop() # get last of most frequent elements
        self.numCount[frequent_last] -= 1

        if len(self.count[self.maxCount]) == 0: # no more elements at that frequency
            self.maxCount -= 1
        return frequent_last

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()