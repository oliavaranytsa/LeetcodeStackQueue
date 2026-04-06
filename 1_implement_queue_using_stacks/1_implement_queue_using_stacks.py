class MyQueue:

    class Stack:
        def __init__(self):
            self._top = None

        def push(self, x):
            self._top = (x, self._top)

        def pop(self):
            val, self._top = self._top
            return val

        def peek(self):
            return self._top[0]

        def is_empty(self):
            return self._top is None

    def __init__(self):
        self.stack1 = MyQueue.Stack()
        self.stack2 = MyQueue.Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()