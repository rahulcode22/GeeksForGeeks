class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if self.items is None:
            return None
        return self.items[-1]

    def isEmpty(self):
        return self.items == []


def isBalanced(expression):
    s = Stack()
    balanced = True
    index = 0
    while index < len(expression) and balanced:
        symbol = expression[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            top = s.pop()
            if not matches(top,symbol):
                balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = '[{('
    closers = ']})'
    return opens.index(open) == closers.index(close)

print isBalanced('{([])}')
