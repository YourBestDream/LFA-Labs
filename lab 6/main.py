import matplotlib.pyplot as plt
import networkx as nx
from classes.Lexer import Lexer
from classes.Parser import Parser

def visualize_ast(root):
    G = nx.DiGraph()  # Directed graph to represent the AST
    root.add_to_graph(G)
    pos = nx.spring_layout(G, seed=42)  # Use a fixed seed for consistent layouts
    labels = {node: G.nodes[node]['label'] for node in G.nodes()}
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_color='darkred')
    plt.show()

def main():
    text = "3 + 5 - ( 7 - 2 )"
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.expr()
    visualize_ast(ast)  # Call to visualize the AST

if __name__ == "__main__":
    main()
