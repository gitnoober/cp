from heapq import heapify, heappush, heappop
from collections import defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.use_dict = {}
        self.cache_heap = []  # use, time, key
        self.dict = {}
        self.time = 0
        self.len = 0
        self.times = defaultdict(int)
        heapify(self.cache_heap)

    def get(self, key: int) -> int:
        self.time += 1
        if key in self.dict:
            self.use_dict[key] += 1
            heappush(self.cache_heap, (self.use_dict[key], self.time, key))
            self.times[key] += 1
            print(key, "key")
            # print(self.cache_heap, "cache_heap")
            # print(self.use_dict, "use_dict")
            # print(self.dict, "dict")
            # print(self.times, "times")
            # print(self.capacity, "capacity")
            # print()
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # print(key, value, "key value before")
        self.time += 1
        if key in self.use_dict:
            self.use_dict[key] += 1
            self.dict[key] = value
            self.times[key] += 1
            heappush(self.cache_heap, (self.use_dict[key], self.time, key))
            # return

        elif self.len < self.capacity:
            self.dict[key] = value
            if key in self.use_dict:
                self.use_dict[key] += 1
            else:
                self.use_dict[key] = 1
                self.len += 1
            counter = self.use_dict[key]
            self.times[key] += 1
            heappush(self.cache_heap, (counter, self.time, key))
        else:
            while self.cache_heap:
                counter, use_times, keyy = heappop(self.cache_heap)
                if self.times[keyy] == 1:
                    self.times[keyy] -= 1

                    del self.use_dict[keyy]
                    del self.dict[keyy]
                    del self.times[keyy]

                    self.use_dict[key] = 1
                    self.dict[key] = value
                    self.times[key] += 1
                    heappush(self.cache_heap, (1, self.time, key))
                    break
                else:
                    self.times[keyy] -= 1
        # print(key, value, "key value")
        # print(self.cache_heap, "cache_heap")
        # print(self.use_dict, "use_dict")
        # print(self.dict, "dict")
        # print(self.times, "times")
        # print(self.capacity, "capacity")
        # print()


# Your LFUCache object will be instantiated and called as such:
operations = [
    "LFUCache",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "put",
    "get",
    "get",
    "get",
]
keys = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
capacity = keys[0][0]

operations = ["LFUCache", "put", "put", "put", "put", "get"]
keys = [[2], [3, 1], [2, 1], [2, 2], [4, 4], [2]]
capacity = keys[0][0]

obj = LFUCache(capacity)
for r in range(len(operations)):
    operation = operations[r]
    if operation == "put":
        x, y = keys[r]
        obj.put(x, y)
    elif operation == "get":
        val = keys[r][0]
        ans = obj.get(val)
        print(val, ans, "anssssssssss")

# param_1 = obj.get(key)
# obj.put(key,value)
