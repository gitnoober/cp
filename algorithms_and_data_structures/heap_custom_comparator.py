import heapq

# SUBMIT IN PYTHON(FASTER IN PYTHON) NOT PYPY


class MyHeap(object):
    def __init__(self, initial=None, key=lambda x, y: (-(y - x + 1), x)):
        self.key = key
        self.index = 0

        if initial:
            self._data = [(key(item), i, item) for i, item in enumerate(initial)]
            self.index = len(self._data)
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        # print(item, self.key(item[0], item[1]))
        heapq.heappush(self._data, (self.key(item[0], item[1]), self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._data)[2]
