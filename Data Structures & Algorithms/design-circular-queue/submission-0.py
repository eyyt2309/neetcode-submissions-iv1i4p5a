class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.qlen = k
        self.start = None
        self.end = None
        self.numElements = 0

    def enQueue(self, value: int) -> bool:
        if self.end == None: # initalize circular queue
            self.queue[0] = value
            self.end = 0
            self.start = 0
            self.numElements += 1
        else:
            if self.numElements == self.qlen:
                return False
            new_end = (self.end + 1) % self.qlen # new index end modulus by queue size
            self.queue[new_end] = value
            self.end = new_end
            self.numElements += 1
        return True


    def deQueue(self) -> bool:
        if self.numElements == 0:
            return False
        else:
            self.numElements -= 1
            self.start = (self.start + 1) % self.qlen
        return True

    def Front(self) -> int:
        if self.numElements == 0:
            return -1
        else:
            return self.queue[self.start]

    def Rear(self) -> int:
        if self.numElements == 0:
            return -1
        else:
            return self.queue[self.end]      

    def isEmpty(self) -> bool:
        return self.numElements == 0

    def isFull(self) -> bool:
        return self.numElements == self.qlen


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()