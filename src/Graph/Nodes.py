"""
Package used to create basic oriented graphs.
"""


class Node:
    """A node is the basic component of a graph and allows for graph construction."""

    def __init__(self, name):
        """Creates a new node"""
        self.name = name
        self.s_manager = SuccessorManager()

    def get_children(self):
        return self.s_manager

    def add(self, successor, cost: int = 1):
        self.s_manager.add(successor, cost)

    def remove(self, to_remove):
        self.s_manager.remove(to_remove)

    def nb_next(self):
        return len(self.s_manager)

    def __str__(self):
        return self.name

    __repr__ = __str__

    def graph_size(self, to_ignore: list = None) -> int:
        if to_ignore is None:
            to_ignore = []
        if self not in to_ignore:
            to_ignore.append(self)
            res = 1
            for following in self.get_children():
                res += following.graph_size(to_ignore)
            return res
        return 0


class SuccessorManager:
    """This class manages the successors of a node"""

    def __init__(self):
        self.successors = []
        self.costs = {}

    def __iter__(self):
        return self.successors.__iter__()

    def add(self, successor: Node, cost: int = 1):
        self.successors.append(successor)
        self.costs[successor] = cost

    def remove(self, to_remove: Node):
        self.successors.remove(to_remove)

    def get_cost(self, to_find: Node):
        if to_find in self.costs.keys():
            return self.costs[to_find]
        raise KeyError("The requested node is not a successor")

    def __len__(self):
        return len(self.successors)





