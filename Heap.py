import copy


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

    def size(self):
        return len(self.ordered_path)

    def remove(self, x):
        self.ordered_path.remove(x)

    def trim(self, value):

        if self.size() > value:

            path_copy = copy.copy(self.ordered_path)  # make a shallow copy of ordered path
            path_copy.sort(key=lambda x: x.get_end_heuristic(), reverse=False)

            for p in path_copy:
                if path_copy.index(p) > value-1:
                    # print("Trimming: " + p.str_heuristic())
                    self.ordered_path.remove(p)


    def push(self, x):  # sort by the path cost, used by UCS
        self.ordered_path.append(x)
        self.ordered_path.sort(key=lambda x: x.cost, reverse=False)
        self.uc_sort_same_value()

    def push_heuristic(self, x):  # sort by heuristic of the end node, used by GS
        self.ordered_path.append(x)
        self.ordered_path.sort(key=lambda x: x.get_end_heuristic(), reverse=False)
        self.gs_sort_same_value()

    def push_a_star(self, x):  # sort by heuristic plus cost, used by AS
        self.ordered_path.append(x)
        self.ordered_path.sort(key=lambda x: (x.get_end_heuristic() + x.get_cost()), reverse=False)
        self.as_delete_path()
        self.as_sort_same_value()

    def push_hc(self, x):  # used by HC, and BMS

        self.ordered_path.insert(0, x)
        # print("Pushing: " + x.str_heuristic())

        # self.ordered_path.append(x)

        # path_copy = copy.copy(self.ordered_path)  # make a shallow copy of ordered path
        # path_copy.sort(key=lambda x: x.get_end_heuristic(), reverse=False)

        # first = path_copy[0]
        # print("First is: " + first.str_heuristic())
        # print(first)
        # self.ordered_path.remove(first)

        # self.ordered_path.insert(0, first)

    def push_bms(self, x):
        self.ordered_path.append(x)

    def hc_sort(self):
        path_copy = copy.copy(self.ordered_path)  # make a shallow copy of ordered path
        path_copy.sort(key=lambda x: x.get_end_heuristic(), reverse=False)

        first = path_copy[0]

        self.ordered_path.remove(first)
        self.ordered_path.insert(0, first)

    def heuristic_sort(self):  # used by BMS
        self.ordered_path.sort(key=lambda x: x.get_end_heuristic(), reverse=False)
        self.gs_sort_same_value()

    def pop(self):
        removed = self.ordered_path[0]
        self.ordered_path.remove(removed)
        return removed

    def get_left_peek(self):
        if self.ordered_path:
            return self.ordered_path[0]
        else:
            return None

    def uc_sort_same_value(self):
        for index in range(len(self.ordered_path)-1):  # sort path with the same cost alphabetically
            if self.ordered_path[index].cost == self.ordered_path[index+1].cost:
                first = self.ordered_path[index]
                second = self.ordered_path[index + 1]

                if first.get_end_id() > second.get_end_id():
                    a, b = index, index + 1
                    self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]
                elif first.get_end_id() == second.get_end_id():  # if the two path ends at the same node
                    # print("Here")
                    if first.get_vertexes_count() > second.get_vertexes_count():
                        a, b = index, index + 1
                        self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]
                    # sort the path in lexicographic order
                    elif first.get_vertexes_count() == second.get_vertexes_count():
                        if first.get_vertexes_id_string() > second.get_vertexes_id_string():
                            a, b = index, index + 1
                            self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]

    def gs_sort_same_value(self):
        for index in range(len(self.ordered_path)-1):  # sort path with the same cost alphabetically
            if self.ordered_path[index].get_end_heuristic() == self.ordered_path[index+1].get_end_heuristic():
                # the only part that is different
                first = self.ordered_path[index]
                second = self.ordered_path[index + 1]

                if first.get_end_id() > second.get_end_id():
                    a, b = index, index + 1
                    self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]
                elif first.get_end_id() == second.get_end_id():  # if the two path ends at the same node
                    # print("Here")
                    if first.get_vertexes_count() > second.get_vertexes_count():
                        a, b = index, index + 1
                        self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]
                    # sort the path in lexicographic order
                    elif first.get_vertexes_count() == second.get_vertexes_count():
                        if first.get_vertexes_id_string() > second.get_vertexes_id_string():
                            a, b = index, index + 1
                            self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]

    def as_sort_same_value(self):
        for index in range(len(self.ordered_path)-1):  # sort path with the same cost alphabetically
            # the only part that is different
            if self.ordered_path[index].get_end_heuristic() + self.ordered_path[index].cost \
                    == self.ordered_path[index+1].get_end_heuristic() + self.ordered_path[index+1].cost:
                first = self.ordered_path[index]
                second = self.ordered_path[index + 1]

                if first.get_end_id() > second.get_end_id():
                    a, b = index, index + 1
                    self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]
                elif first.get_end_id() == second.get_end_id():  # if the two path ends at the same node
                    # print("Here")
                    if first.get_vertexes_count() > second.get_vertexes_count():
                        a, b = index, index + 1
                        self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]
                    # sort the path in lexicographic order
                    elif first.get_vertexes_count() == second.get_vertexes_count():
                        if first.get_vertexes_id_string() > second.get_vertexes_id_string():
                            a, b = index, index + 1
                            self.ordered_path[b], self.ordered_path[a] = self.ordered_path[a], self.ordered_path[b]

    def as_delete_path(self):
        for p in self.ordered_path:
            for other in self.ordered_path:
                if p != other:

                    if p.get_end() == other.get_end():  # the two paths have the same end
                        if p.get_end_heuristic() + p.cost > other.get_end_heuristic() + other.cost:
                            self.ordered_path.remove(p)
                            return
                        elif p.get_end_heuristic() + p.cost < other.get_end_heuristic() + other.cost:
                            self.ordered_path.remove(other)
                            return
