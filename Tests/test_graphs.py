from unittest import TestCase

from POG.Graphs import Graph
from POG.Nodes import Node


class TestGraph(TestCase):
    def test_graph_str(self):
        a = Node("A")
        b = Node("B")
        graph = Graph(a, b)
        self.assertEqual(str(graph), "A (successors: [])\nB (successors: [])\n")

    def test_graph_str_successors(self):
        a = Node("A")
        b = Node("B")
        a.add(b)
        graph = Graph(a, b)
        self.assertEqual(str(graph), "A (successors: [B])\nB (successors: [])\n")

    def test_graph_generate_mermaid(self):
        a = Node("A")
        b = Node("B")
        a.add(b)
        graph = Graph(a, b)
        self.assertEqual(len(graph.export_to_mermaid()), 47)
        # testing size instead of string itself because of the length of it
