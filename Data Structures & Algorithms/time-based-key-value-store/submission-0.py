class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
            self.hashmap[key].append((timestamp, value))
            self.hashmap[key].sort()
        else:
            self.hashmap[key].append((timestamp, value))
            self.hashmap[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            for i in range(len(self.hashmap[key]) - 1, -1, -1):
                if timestamp >= self.hashmap[key][i][0]:
                    return self.hashmap[key][i][1]

        return ""

        