class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        returning = ""
        value = []
        if self.keys.get(key) is not None:
            value = self.keys.get(key)

        left = 0
        right = len(value) - 1
        while left <= right:
            middle = (left + right) // 2
            
            if value[middle][1] <= timestamp:
                returning = value[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return returning
        
