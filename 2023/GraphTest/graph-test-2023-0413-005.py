import networkx as nx
from pyvis.network import Network

# Create a directed graph
G = nx.DiGraph()

# Add some nodes and edges
G.add_nodes_from([1,2,3,4,5,6])
G.add_edge(1,2)
G.add_edge(3,2)
G.add_edge(5,4)
G.add_edge(5,6)
G.add_edge(4,1)
G.add_edge(2,5)
G.add_edge(6,3)

# Detect orphaned nodes
orphaned_nodes = [n for n in G.nodes() if G.in_degree(n) == 0 and G.out_degree(n) == 0]
print("Orphaned nodes: ", orphaned_nodes)

# Detect looped nodes
looped_nodes = list(nx.simple_cycles(G))
print("Looped nodes: ", looped_nodes)

cycles = nx.find_cycle(G)
print(f'cycles = {cycles}')

#Create a Pyvis Network object:
net=Network(notebook=True,directed=True)
#Add nodes to the network:
for node in G.nodes():
    net.add_node(node,label=f'{node}')
#Add edges to the network:
for edge in G.edges():
    net.add_edge(edge[0], edge[1])
#Display the network:
net.show('example.html')
