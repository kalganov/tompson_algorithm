import argparse
import pydot
from graphviz import Digraph

parser = argparse.ArgumentParser()
parser.add_argument("file", help="dot file with graph")
args = parser.parse_args()

(graph,) = pydot.graph_from_dot_file(args.file)

terminals = [0]
char_to_matrix = {}
matrix_to_char = {}
E = set()
nodes = []
start_node = None
for source_node in graph.get_node_list():
    if source_node.get_attributes().get("start") == "true":
        start_node = source_node.get_name()
        break

for edge in graph.get_edge_list():
    for char in edge.get_attributes().get('label').replace('"', "").split(','):
        E.add(char)

P = [[start_node]]
Q = set()
Edges = []

g = Digraph('G', filename='answer.gv')
g.attr(rankdir='LR', size='8,5')

while P:
    P_d = P.pop()
    for char in E:
        Q_d = set()
        for p in P_d:
            for edge in graph.get_edge_list():
                if edge.get_source() == p and char in edge.get_attributes().get('label').replace('"', "").split(','):
                    Q_d.add(edge.get_destination())
        Q_d_name = ','.join(Q_d)
        P_d_name = ','.join(P_d)
        is_existed_edge = False
        for new_edge in Edges:
            if new_edge.get_source() == P_d_name and new_edge.get_destination() == Q_d_name:
                new_label = set(new_edge.get_attributes().get('label').split(","))
                new_label.add(char)
                new_label = ",".join(new_label)
                new_edge.get_attributes().update({'label': new_label})
                is_existed_edge = True
        if not is_existed_edge:
            Edges.append(pydot.Edge(P_d_name, Q_d_name, label=char))
        if Q_d_name and Q_d_name not in Q:
            P.append(Q_d)
            Q.add(Q_d_name)
            g.node(Q_d_name)

for edge in Edges:
    g.edge(edge.get_source(), edge.get_destination(), edge.get_attributes().get('label'))

g.view()

g.render()
