class TimeMap:

    def __init__(self):
        # set up the persons attributes, name, mood and time
        self.startMap = defaultdict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # store (name(key), mood, time)
        if key not in self.startMap:
            self.startMap[key] = []
        self.startMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # returns the mood of the person at a time
        # this is where the binary search will be necessary to locate the time specified
        res, values = "", self.startMap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        

        
