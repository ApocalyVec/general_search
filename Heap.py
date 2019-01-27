
class Heap:
    def __init__(self):
        self.ordered_path = []

    def __str__(self): # really mess around with printed queue to match requirement

        return str([str(p) for p in self.ordered_path]).replace("'", "")
        # return str([str([i.id for i in x]).replace("[", "<").replace("]", ">").replace("'", "")
        #             for x in self.elements]).replace("'", "")

    def isEmpty(self):
        return len(self.ordered_path) == 0

    def push(self, x):
        self.ordered_path.append(x)
        self.ordered_path.sort(key=lambda x: x.cost, reverse=False)

    def pop(self):
        removed = self.ordered_path[0]
        self.ordered_path.remove(removed)
        return removed
