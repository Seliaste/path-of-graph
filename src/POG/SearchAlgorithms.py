from POG.Nodes import Node


def dijsktra(n: Node):
    costs = {n: 0}
    black = []
    grey = [successor for successor in n.get_successors()]
    for successor in n.get_successors():
        costs[successor] = n.get_successors().get_cost(successor)
    while len(grey) != 0:
        curr = min(grey, key=costs.get)
        for successor in curr.get_successors():
            val = costs[curr] + curr.get_successors().get_cost(successor)
            if (successor in black and val < costs[successor]) or successor not in black:
                costs[successor] = val
        black.append(curr)
        grey.remove(curr)
    return costs
