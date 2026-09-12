from collections import deque
class LRUCache:
    class ListNode:
        def __init__(self, val = None, key = None, next = None, prev = None):
            self.val = val
            self.key = key
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None # most recently used
        self.tail = None # least recently used

    def get(self, key: int) -> int:
        if key in self.cache:
            self.shiftToFront(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # create node if empty dict
        if len(self.cache) == 0:
            node = self.ListNode(value, key)
            self.cache[key] = node
            self.head = node
            self.tail = node
        # update key
        elif key in self.cache:
            self.shiftToFront(key)
            self.cache[key].val = value
        else:
            node = self.ListNode(value, key)
            self.cache[key] = node

            # update head
            self.head.next = node
            node.prev = self.head
            self.head = node

            if len(self.cache) > self.capacity:
                last = self.tail
                last_next = last.next
                last_next.prev = None

                self.tail = last_next

                del self.cache[last.key]



    def shiftToFront(self, key):
        key_node = self.cache[key]

        # if node to shift is already at head, return
        if self.head == key_node:
            return

        elif self.tail == key_node:
            next_node = key_node.next
            next_node.prev = None
            self.tail = next_node # update new tail

            head_node = self.head # get curr head
            head_node.next = key_node 
            key_node.prev = head_node
            key_node.next = None

            self.head = key_node # set new head 

        else: # key_node in the middle 
        # prev_node <-> key_node <-> next_node
            prev_node = key_node.prev
            next_node = key_node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            self.head.next = key_node
            key_node.prev = self.head
            key_node.next = None
            self.head = key_node




                    




                







