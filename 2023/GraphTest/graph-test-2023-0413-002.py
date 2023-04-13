import networkx as nx

# Create a directed graph
G = nx.DiGraph([(1,2), (2,3), (3,4), (4,5), (5,6), (6,3)])

# add orphaned node
G.add_node(7)

# check for orphaned and looped nodes
orphans = [n for n, d in G.in_degree() if d == 0]
loops = list(nx.simple_cycles(G))

print("Orphaned nodes:", orphans)
print("Looped nodes:", loops)