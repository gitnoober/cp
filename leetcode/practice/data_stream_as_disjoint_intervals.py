from heapq import heapify, heappush, heappop


class SummaryRanges:
    def __init__(self):
        self.intervals = []
        self.arr = []
        self.clear = True
        self.duplicates = set()
        heapify(self.intervals)

    def addNum(self, value: int):
        if value in self.duplicates:
            return
        heappush(self.intervals, value)
        self.duplicates.add(value)
        self.clear = False

    def reconstruct_arr(self):
        self.arr.clear()
        push_back = []
        while self.intervals:
            start = heappop(self.intervals)
            push_back.append(start)
            end = start
            prev = start
            while self.intervals:
                nxt = heappop(self.intervals)
                if nxt - 1 == prev:
                    end = nxt
                    push_back.append(nxt)
                else:
                    heappush(self.intervals, nxt)
                    break
                prev = nxt
            self.arr.append([start, end])

        for val in push_back:
            heappush(self.intervals, val)

    def getIntervals(self):
        if self.clear:
            return self.arr
        self.reconstruct_arr()
        return self.arr


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
input_arr = [
    "SummaryRanges",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
]
input_arr = [
    "SummaryRanges",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
]

# vals = [[], [1], [], [3], [], [7], [], [2], [], [6], []]
"""
[6,6], 
"""

vals = [
    [],
    [6],
    [],
    [6],
    [],
    [0],
    [],
    [4],
    [],
    [8],
    [],
    [7],
    [],
    [6],
    [],
    [4],
    [],
    [7],
    [],
    [5],
    [],
]
for r in range(len(input_arr)):
    func = input_arr[r]
    val = vals[r]
    if func == "addNum":
        val = val[0]
        obj.addNum(val)
    elif func == "getIntervals":
        x = obj.getIntervals()
        print(x, "x")


# obj.addNum(value)
# param_2 = obj.getIntervals()
