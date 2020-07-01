class CQueue:

    def __init__(self):
        self._add_stack = []
        self._delete_stack = []

    def appendTail(self, value: int) -> None:

        if len(self._delete_stack) == 0:
            self._add_stack.append(value)
        else:
            while len(self._delete_stack) > 0:
                self._add_stack.append(self._delete_stack.pop())
            self._add_stack.append(value)

    def deleteHead(self) -> int:
        if len(self._add_stack) == 0:
            if len(self._delete_stack) == 0:
                return -1
            else:
                return self._delete_stack.pop()
        else:
            while len(self._add_stack) > 0:
                self._delete_stack.append(self._add_stack.pop())
            return self._delete_stack.pop()

if __name__ == "__main__":
    q = CQueue()
    print(q.deleteHead())
    q.appendTail(5)
    q.appendTail(2)
    print(q.deleteHead())
    print(q.deleteHead())


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()