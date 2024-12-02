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

    def get_list(self):
        return list(self.items)


if __name__ == '__main__':
    my_stack = Stack()

    test_cases = [my_stack.is_empty(), my_stack.push('new_item'), my_stack.push(0),
                  my_stack.push(13), my_stack.pop(), my_stack.peek(), my_stack.size()]

    for case in test_cases:
        print(case)