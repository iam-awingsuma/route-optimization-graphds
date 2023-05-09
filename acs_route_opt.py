import networkx as nx
import matplotlib.pyplot as plt
from bokeh.palettes import Spectral

# create a directed graph to represent airline routes
G = nx.DiGraph()
# add nodes to the graph representing cities
G.add_nodes_from(["Singapore", "New York", "Tokyo", "Manila", "Dubai", "Milan"])
# add edges to the nodes representing the routes between cities
G.add_edges_from(
    [
        ("Singapore", "New York", {"weight": 18.30}),
        ("Singapore", "Dubai", {"weight": 7.26}),
        ("Singapore", "Tokyo", {"weight": 6.55}),
        ("New York", "Tokyo", {"weight": 14.7}),
        ("New York", "Dubai", {"weight": 13.29}),
        ("New York", "Milan", {"weight": 9.1}),
        ("Tokyo", "Manila", {"weight": 4.48}),
        ("Tokyo", "Dubai", {"weight": 10.40}),
        ("Milan", "Dubai", {"weight": 6.18}),
        ("Manila", "Dubai", {"weight": 8.58}),
        ("Milan", "Singapore", {"weight": 12.15}),
        ("Milan", "New York", {"weight": 9.1}),
        ("Dubai", "Singapore", {"weight": 7.26}),
        ("Dubai", "New York", {"weight": 13.29})
    ]
)

plt.figure(figsize=(8, 6))

pos = nx.circular_layout(G)

options = {
    'node_color': Spectral[6], # first 5 colors from the Spectral palette
    'node_size': 3500,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 18,
    'edge_color': 'blue',
}

nx.draw(G, pos, with_labels=True, font_size=8, arrows=True, **options)

nx.draw_networkx_edge_labels(G, pos,
                             edge_labels={
                                 ("Singapore", "New York"): "18h 30m flight",
                                 ("Singapore", "Dubai"): "7h 31m flight",
                                 ("Singapore", "Tokyo"): "6h 55m flight",
                                 ("Tokyo", "Manila"): "4h 48m flight",
                                 ("Tokyo", "Dubai"): "10h 40m flight",
                                 ("New York", "Tokyo"): "14h 7m flight",
                                 ("New York", "Dubai"): "13h 29m flight",
                                 ("New York", "Milan"): "7h 59m flight",
                                 ("Manila", "Dubai"): "8h 58m flight",
                                 ("Milan", "Singapore"): "12h 15m flight",
                                 ("Milan", "Dubai"): "6h 18m flight",
                                 ("Milan", "New York"): "9h 1m flight",
                                 ("Dubai", "Singapore"): "7h 26m flight",
                                 ("Dubai", "New York"): "13h 29m flight"
                             },
                             font_color='red', font_size=8,
                            )

ax = plt.gca()
ax.collections[0].set_edgecolor("#000000")

# find the shortest path between two nodes using Dijkstra's algorithm
path = nx.dijkstra_path(G, "Manila", "Milan")

# print the shortest path
print("The shortest path from", path[0], "to", path[len(path)-1], "would be")
shortest_path = [f"-> {path[i]} " for i in range(len(path))]
print("".join(shortest_path))

plt.show()

