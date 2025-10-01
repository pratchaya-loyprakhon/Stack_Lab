class Stack:
    def __init__(self):
        self._list = []

    def is_empty(self):
        return self._list == []

    def push(self,item):
        self._list.append(item)

    def pop(self):
        if self.is_empty():
            return IndexError(Stack Is Empty!)
        return self._list.pop()

    def peek(self):
        if self.is_empty():
            return IndexError(Stack Is Empty!)
        return self._list[-1]

    def size(self):
        return len(self._list)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(Size after push:  , s.size())
print(Top element:  , s.peek())

print(Pop: , s.pop())
print(Pop: , s.pop())
print(Pop: , s.pop())
print(Pop: , s.pop())
print(Pop: , s.pop())

print(Is empty? , s.is_empty())
print(Pop from empty:  , s.pop())
