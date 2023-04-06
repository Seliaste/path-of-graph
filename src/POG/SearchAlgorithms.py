"""Implementation of multiple search algorithms"""
from POG.Nodes import Node


def dijkstra_distances(n: Node):
    """Returns a dictionary with all accessible nodes and the distance to them."""
    distance = {n: 0}
    black = []
    grey = [successor for successor in n.get_successors()]
    for successor in n.get_successors():
        distance[successor] = n.get_successors().get_cost(successor)
    while len(grey) != 0:
        curr = min(grey, key=distance.get)
        for successor in curr.get_successors():
            val = distance[curr] + curr.get_successors().get_cost(successor)
            if (successor in black and val < distance[successor]) or successor not in black:
                distance[successor] = val
        black.append(curr)
        grey.remove(curr)
    return distance


def dijkstra_pathfinding(start: Node, end: Node):
    """Returns a list of the nodes from start to end. If no path is found, returns an empty list"""
    distance = {start: 0}
    previous = {start: None}
    black = []
    grey = [successor for successor in start.get_successors()]
    for successor in start.get_successors():
        distance[successor] = start.get_successors().get_cost(successor)
        previous[successor] = start
    while len(grey) != 0:
        curr = min(grey, key=distance.get)
        for successor in curr.get_successors():
            val = distance[curr] + curr.get_successors().get_cost(successor)
            if (successor in black and val < distance[successor]) or successor not in black:
                distance[successor] = val
                previous[successor] = curr
        black.append(curr)
        grey.remove(curr)
    if end not in previous.keys():
        return []
    # Now we reverse the previous path
    res = []
    u = end
    while u is not None:
        res.append(u)
        u = previous[u]
    res.reverse()
    return res
