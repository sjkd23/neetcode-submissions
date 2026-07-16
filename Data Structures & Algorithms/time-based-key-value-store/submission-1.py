class TimeMap:

    def __init__(self):
        self.entries = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.entries:
            self.entries[key] = []
        
        self.entries[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        result = ""
        if key not in self.entries:
            return result

        left = 0
        right = len(self.entries[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            stored_timestamp = self.entries[key][mid][1]
            value = self.entries[key][mid][0]
            if stored_timestamp == timestamp:
                return value
            elif stored_timestamp < timestamp:
                result = value
                left = mid + 1
            else:
                right = mid - 1
        return result

        
