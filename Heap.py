class Heap:
    def __init__(self):
        self.ordered_path = []  # path objects

    def __str__(self):  # really mess around with printed queue to match requirement

        return str([str(p) for p in self.ordered_path]).replace("'", "")

    def str_heuristic(self):  # used by Greedy search
        return str([str(p.str_heuristic()) for p in self.ordered_path]).replace("'", "")

    def str_a_star(self):  # used by A* search
        return str([str(p.str_a_star()) for p in self.ordered_path]).replace("'", "")

    def isEmpty(self):
        return len(self.ordered_path) == 0

    def push(self, x):  # sort by the path cost
        self.ordered_path.append(x)
        self.ordered_path.sort(key=lambda x: x.cost, reverse=False)

    def push_heuristic(self, x):  # sort by heuristic of the end node, used by Greedy search
        self.ordered_path.append(x)
        self.ordered_path.sort(key=lambda x: x.get_end_heuristic(), reverse=False)

    def push_a_star(self, x):  # sort by heuristic plus cost, used by A* search
        self.ordered_path.append(x)
        self.ordered_path.sort(key=lambda x: (x.get_end_heuristic() + x.get_cost()), reverse=False)

    def pop(self):
        removed = self.ordered_path[0]
        self.ordered_path.remove(removed)
        return removed

    def get_left_peek(self):
        if self.ordered_path:
            return self.ordered_path[0]
        else:
            return None
