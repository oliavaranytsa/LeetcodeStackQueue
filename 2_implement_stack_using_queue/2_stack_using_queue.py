class MyStack:

    class Queue:
        class _Node:
            def __init__(self, val):
                self.val = val
                self.next = None

        def __init__(self):
            self._head = None
            self._tail = None
            self._size = 0

        def push(self, x):
            node = self._Node(x)
            if self._tail:
                self._tail.next = node
            else:
                self._head = node
            self._tail = node
            self._size += 1

        def pop(self):
            val = self._head.val
            self._head = self._head.next
            if not self._head:
                self._tail = None
            self._size -= 1
            return val

        def peek(self):
            return self._head.val

        def size(self):
            return self._size

        def is_empty(self):
            return self._head is None

    def __init__(self):
        self.queue1 = MyStack.Queue()
        self.queue2 = MyStack.Queue()

    def push(self, x: int) -> None:
        self.queue1.push(x)

    def pop(self) -> int:
        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())
        val = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    def top(self) -> int:
        while not self.queue1.is_empty():
            val = self.queue1.pop()
            self.queue2.push(val)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    def empty(self) -> bool:
        return self.queue1.is_empty()