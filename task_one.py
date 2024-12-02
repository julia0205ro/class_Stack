class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Attempt to remove an element from an empty stack')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Attempt to retrieve the top element of an empty stack')
        return self.items[-1]

    def size(self):
        return len(self.items)

    # def remove(self, param):
    #     return self.items.remove(param)

    def get_list(self):
        return list(self.items)


if __name__ == '__main__':
    a = Stack()
    print(a.is_empty())
    a.push('new_item')
    a.push(0)
    a.push(13)
    print(a.pop())
    print(a.peek())
    print(a.size())