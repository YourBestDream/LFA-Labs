import networkx as nx
import matplotlib.pyplot as plt

class ASTNode:
    def add_to_graph(self, graph, parent=None):
        pass  # Base class does nothing

class BinaryOperator(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def add_to_graph(self, graph, parent=None):
        # Create a node with a descriptive label
        operator_label = f"{self.operator} (BinaryOperator)"
        operator_node = f"{self.operator}_{id(self)}"
        graph.add_node(operator_node, label=operator_label)
        if parent:
            graph.add_edge(parent, operator_node)

        # Recursively add children with their respective labels
        self.left.add_to_graph(graph, operator_node)
        self.right.add_to_graph(graph, operator_node)

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

    def add_to_graph(self, graph, parent=None):
        value_label = f"Value: {self.value}"
        value_node = f"Number_{self.value}_{id(self)}"
        graph.add_node(value_node, label=value_label)
        if parent:
            graph.add_edge(parent, value_node)
