"""A graph is a collection of nodes"""
from POG.Nodes import Node


class Graph:
    def __init__(self, *nodes):
        self.nodes = [node for node in nodes]

    def add(self, node: Node):
        self.nodes.append(node)

    def remove(self, node: Node):
        self.nodes.remove(node)

    def export_to_mermaid(self):
        res = "graph TD;\n"
        for node in self.nodes:
            res += "    " + node.name + "((" + node.name + "))\n"
            for successor in node.get_successors():
                res += "    " + node.name + " --" + str(node.get_successors().get_cost(successor)) \
                       + "--> " + successor.name + "\n"
        print(res)
        return res

    def __str__(self):
        res = ""
        for node in self.nodes:
            res += str(node) + " (successors: " + str(node.get_successors()) + ")\n"
        return res

    def __len__(self):
        return self.nodes.__len__()
