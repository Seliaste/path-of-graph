from unittest import TestCase

from Graph.Nodes import Node
from Graph.SearchAlgorithms import dijsktra


class Test(TestCase):
    def test_dijsktra(self):
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

        self.assertEqual(dijsktra(a), {a: 0, d: 2, e: 3, c: 7, b: 10})

    def test_dijsktra_small(self):
        a = Node("A")

        self.assertEqual(dijsktra(a), {a: 0})

