import collections


class Path:
    def __init__(self):
        self.vertexes = collections.deque()
        self.cost = 0

    def __str__(self):
        return str(self.cost) + \
               str([v.id for v in self.vertexes]).replace("'", "").replace("[", "<").replace("]", ">")
        # return str([str([i.id for i in x]).replace("[", "<").replace("]", ">").replace("'", "")
        #             for x in self.elements]).replace("'", "")

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def get_vertexes(self):
        return list(self.vertexes)

    def get_start(self):
        if self.vertexes:
            return self.vertexes[-1]
        else:
            return None

    def get_end(self):
        if self.vertexes:
            return self.vertexes[0]
        else:
            return None

    def add_vertex(self, x):
        #  add the cost

        # print(self.vertexes[-1])

        if len(self.vertexes) >= 1:
            self.cost = self.cost + float(self.get_end().get_weight(x))

        self.vertexes.appendleft(x)

