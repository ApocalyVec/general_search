#adapted from https://www.redblobgames.com/pathfinding/a-star/implementation.html

import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def emptu(self):
        return len(self.elements) == 0

    def push(self, x):
        self.elements.appendo(x)

    def pop(self):
        return self.elements.popleft()
