import collections
import math


class Path:
    def __init__(self):
        self.vertexes = collections.deque()
        self.cost = 0

    def __str__(self):  # used by UCS
        return str(int(self.cost)) + \
               str([v.id for v in self.vertexes]).replace("'", "").replace("[", "<").replace("]", ">")
        # return str([str([i.id for i in x]).replace("[", "<").replace("]", ">").replace("'", "")
        #             for x in self.elements]).replace("'", "")

    def str_heuristic(self):  # used by GS
        return str(self.get_end_heuristic()) + \
               str([v.id for v in self.vertexes]).replace("'", "").replace("[", "<").replace("]", ">")

    # def str_a_star(self):  # used by AS
    #     return str(self.get_end_heuristic() + self.cost) + \
    #            str([v.id for v in self.vertexes]).replace("'", "").replace("[", "<").replace("]", ">")

    def str_a_star(self):  # used by AS
        return 'f=' + str(int(self.get_end_heuristic())) + '+' + str(int(self.cost)) + '=' +str(int(self.get_end_heuristic() + self.cost)) + \
               str([v.id for v in self.vertexes]).replace("'", "").replace("[", "<").replace("]", ">")

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def get_vertexes(self):
        rtn = list(self.vertexes)
        rtn.reverse()  # must reverse for the new path to work
        return rtn

    def get_vertexes_count(self):
        return len(list(self.vertexes))

    def get_vertexes_id_string(self):
        rtn = ""
        for v in self.get_vertexes():
            rtn = rtn + v.id
        return rtn

    def get_cost(self):
        return self.cost

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

    def get_end_id(self):
        if self.vertexes:
            return self.get_end().id
        else:
            return None

    def get_end_heuristic(self):
        if self.vertexes:
            return self.get_end().get_heuristic()
        else:
            return math.inf

    def add_vertex(self, x):
        #  add the cost

        # print(self.vertexes[-1])

        if len(self.vertexes) >= 1:
            self.cost = self.cost + float(self.get_end().get_weight(x))

        self.vertexes.appendleft(x)

