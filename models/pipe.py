
class Pipe():
    def __init__(self, func, position, next=None):
        self.func = func
        self.position = position
        self.next = next
