import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add some nodes and edges
G.add_nodes_from([1,2,3,4,5])
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,1)
G.add_edge(4,2)
G.add_node(5)

# Detect orphaned nodes
orphaned_nodes = [n for n in G.nodes() if G.in_degree(n) == 0 and G.out_degree(n) == 0]
print("Orphaned nodes: ", orphaned_nodes)

# Detect looped nodes
looped_nodes = [n for n in nx.simple_cycles(G)]
print("Looped nodes: ", looped_nodes)
