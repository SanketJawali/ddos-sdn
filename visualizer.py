import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import networkx as nx

# Topology Visuzlizer
def visualize_topology(topo):
    graph = nx.Graph()

    # Add nodes
    for node in topo.nodes():
        graph.add_node(node)

    # Add links
    for node1, node2 in topo.links():
        graph.add_edge(node1, node2)

    # Categorize nodes
    controllers = [
        node for node in graph.nodes()
        if node.startswith("c")
    ]

    switches = [
        node for node in graph.nodes()
        if node.startswith("s")
    ]

    hosts = [
        node for node in graph.nodes()
        if node.startswith("h")
    ]

    # --------------------------------------------------
    # Position nodes hierarchically
    # --------------------------------------------------

    positions = {}

    # Controllers - top
    for i, controller in enumerate(controllers):
        x = (i - (len(controllers) - 1) / 2) * 2
        positions[controller] = (x, 2)

    # Switches - middle
    for i, switch in enumerate(switches):
        x = (i - (len(switches) - 1) / 2) * 2
        positions[switch] = (x, 1)

    # Hosts - bottom
    for i, host in enumerate(hosts):
        x = (i - (len(hosts) - 1) / 2) * 1.5
        positions[host] = (x, 0)

    # --------------------------------------------------
    # Draw topology
    # --------------------------------------------------

    plt.figure(figsize=(14, 8))

    # Links
    nx.draw_networkx_edges(
        graph,
        positions,
        width=2,
        edge_color="gray"
    )

    # Controllers
    nx.draw_networkx_nodes(
        graph,
        positions,
        nodelist=controllers,
        node_shape="^",
        node_size=1400,
        node_color="orange",
        edgecolors="black",
        linewidths=1.5
    )

    # Switches
    nx.draw_networkx_nodes(
        graph,
        positions,
        nodelist=switches,
        node_shape="s",
        node_size=1400,
        node_color="skyblue",
        edgecolors="black",
        linewidths=1.5
    )

    # Hosts
    nx.draw_networkx_nodes(
        graph,
        positions,
        nodelist=hosts,
        node_shape="o",
        node_size=1100,
        node_color="lightgreen",
        edgecolors="black",
        linewidths=1.5
    )

    # Labels
    nx.draw_networkx_labels(
        graph,
        positions,
        font_size=10,
        font_weight="bold"
    )

    # --------------------------------------------------
    # Legend
    # --------------------------------------------------

    legend_elements = [
        Line2D(
            [0], [0],
            marker="s",
            color="w",
            label="Switch",
            markerfacecolor="skyblue",
            markeredgecolor="black",
            markersize=14
        ),
        Line2D(
            [0], [0],
            marker="o",
            color="w",
            label="Host",
            markerfacecolor="lightgreen",
            markeredgecolor="black",
            markersize=14
        ),
    ]

    plt.legend(
        handles=legend_elements,
        loc="upper right",
        title="Network Components"
    )

    plt.title(
        "SDN Network Topology",
        fontsize=16,
        fontweight="bold"
    )

    plt.axis("off")
    plt.tight_layout()
    plt.show()

