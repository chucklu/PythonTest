import networkx as nx

G = nx.DiGraph([(0, 1), (0, 2), (1, 2)])
result = nx.find_cycle(G, orientation="ignore")
print(result)