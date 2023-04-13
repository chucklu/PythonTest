import networkx as nx

# Create a directed graph
G = nx.DiGraph([(1,2), (2,3), (3,4), (4,5), (5,6), (6,3)])

# add orphaned node
G.add_node(7)

G.add_edges_from([(8,9),(9,8)])

# check for orphaned and looped nodes
orphans = [n for n in G.nodes() if G.in_degree(n) == 0 and G.out_degree(n) == 0]
loops = list(nx.simple_cycles(G))

print("Orphaned nodes:", orphans)
print("Looped nodes:", loops)