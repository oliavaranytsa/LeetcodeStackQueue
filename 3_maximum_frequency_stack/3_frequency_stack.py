from collections import deque


class FreqStack:

    def __init__(self):
        self.stack = deque()
        self.maxfreq = 0

    def push(self, val: int) -> None:
        freq = 0
        for v, f in self.stack:
            if v == val:
                freq = f
        freq += 1

        if freq > self.maxfreq:
            self.maxfreq = freq

        self.stack.append((val, freq))

    def pop(self) -> int:
        temp = deque()
        result = None

        while self.stack:
            val, freq = self.stack.pop()
            if freq == self.maxfreq and result is None:
                result = val
            else:
                temp.appendleft((val, freq))

        self.stack = temp

        self.maxfreq = 0
        for val, freq in self.stack:
            if freq > self.maxfreq:
                self.maxfreq = freq

        return result