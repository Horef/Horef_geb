# imports
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

# definitions
limit = 30

# variables
F = []
F.append(1)
M = []
M.append(0)

F_graph = nx.DiGraph()
M_graph = nx.DiGraph()
Helix = nx.DiGraph()

# logic
for i in range(1, limit):
    M.append(i-F[M[i-1]])
    F.append(i-M[F[i-1]])

for i in range(1, limit):
    M_graph.add_node(i, label=f"{i}")
    M_graph.add_edge(i, M[i])
    F_graph.add_node(i, label=f"{i}")
    F_graph.add_edge(i, F[i])
    Helix.add_node(i, label=f"{i}")
    Helix.add_edge(i, F[i])
    Helix.add_edge(i, M[i])

# output
# subax1 = plt.subplot(111)
# nx.draw(F_graph, pos=nx.kamada_kawai_layout(F_graph), with_labels=True, font_weight='bold')
# subax2 = plt.subplot(111)
# nx.draw(M_graph, pos=nx.kamada_kawai_layout(M_graph), with_labels=True, font_weight='bold')
# subax3 = plt.plot()
# nx.draw(Helix, pos=nx.kamada_kawai_layout(Helix), with_labels=True, font_weight='bold')
# plt.show()

Helix_net = Network()
Helix_net.from_nx(Helix)
Helix_net.show_buttons(filter_=['physics'])
Helix_net.show("Helix.html")

F_net = Network()
F_net.from_nx(F_graph)
F_net.show_buttons(filter_=['physics'])
F_net.show("F.html")

M_net = Network()
M_net.from_nx(M_graph)
M_net.show_buttons(filter_=['physics'])
M_net.show("M.html")