class TimeMap:

    def __init__(self):
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key not in kv dict
        if key not in self.kv:
            self.kv[key] = {}
            self.kv[key][timestamp] = value

        else:
            self.kv[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        else:
            highest_time = float('-inf')
            for time in self.kv[key]:
                if time == timestamp:
                    return self.kv[key][time]
                else:
                    if time < timestamp and time > highest_time:
                        highest_time = time

        if highest_time == float('-inf'):
            return ""
        else:
            return self.kv[key][highest_time]
