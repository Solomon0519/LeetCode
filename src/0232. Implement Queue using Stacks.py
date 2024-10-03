class MyQueue:

    def __init__(self):
        self.queue_stack = []
        self.popped_queue = []
        self.pointer = 0

    def push(self, x: int) -> None:
        self.queue_stack.append(x)

    def pop(self) -> int:
        value = self.queue_stack[self.pointer]
        self.popped_queue.append(value)
        self.pointer += 1
        return value

    def peek(self) -> int:
        return self.queue_stack[self.pointer]

    def empty(self) -> bool:
        return len(self.queue_stack) == len(self.popped_queue)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()