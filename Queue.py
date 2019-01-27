#adapted from https://www.redblobgames.com/pathfinding/a-star/implementation.html

import collections


class Queue:

    def __init__(self):
        self.elements = collections.deque()

    def __str__(self): # really mess around with printed queue to match requirement
        return str([str([i.id for i in x]).replace("[", "<").replace("]", ">").replace("'", "")
                    for x in self.elements]).replace("'", "")

    def isEmpty(self):
        return len(self.elements) == 0

    def push(self, x):
        self.elements.appendleft(x)

    def push_right(self, x):
        self.elements.append(x)

    def pop(self):
        return self.elements.popleft()

    def state(self): # return the first node in the queue if it is not empty
        if self.elements: # check if the queue is empty
            return self.elements[0][0]

    def get_left_peek(self):
        return self.elements[0]

    def get_right_peek(self):
        return self.elements[-1]

