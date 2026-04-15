class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        stackNode = StackNode(val, self.head)
        self.head = stackNode

    def pop(self) -> None:
        if self.head is not None:
            self.head = self.head.next
        else:
            return None
        

    def top(self) -> int:
        if self.head.value is not None:
            return self.head.value
        

    def getMin(self) -> int:
        minimum = float('inf')

        curr = self.head
        if curr is None:
            return 0

        while curr is not None:
            if minimum > curr.value:
                minimum = curr.value
            curr = curr.next
        
        return minimum

class StackNode:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next
        
