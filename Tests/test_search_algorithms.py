from unittest import TestCase

from POG.Nodes import Node
from POG.SearchAlgorithms import dijkstra_distances, dijkstra_pathfinding


class Test(TestCase):
    def test_dijkstra(self):
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")

        a.add(d, 2)
        a.add(e, 3)
        b.add(a, 11)
        c.add(e, 8)
        c.add(a, 1)
        d.add(c, 5)
        e.add(b, 7)

        self.assertEqual(dijkstra_distances(a), {a: 0, d: 2, e: 3, c: 7, b: 10})

    def test_dijkstra_small(self):
        a = Node("A")

        self.assertEqual(dijkstra_distances(a), {a: 0})

    def test_dijkstra_path(self):
        a = Node("A")
        b = Node("B")
        a.add(b)

        self.assertEqual(dijkstra_pathfinding(a, b), [a, b])

    def test_dijkstra_path_long(self):
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")

        a.add(d, 2)
        a.add(e, 3)
        b.add(a, 11)
        c.add(e, 8)
        c.add(a, 1)
        d.add(c, 5)
        e.add(b, 7)

        self.assertEqual(dijkstra_pathfinding(a, b), [a, e, b])

    def test_dijkstra_path_impossible(self):
        a = Node("A")
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")

        a.add(d, 2)
        a.add(e, 3)
        b.add(a, 11)
        c.add(e, 8)
        c.add(a, 1)
        d.add(c, 5)

        self.assertEqual(dijkstra_pathfinding(a, b), [])
