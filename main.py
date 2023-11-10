import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Node:
    def __init__(self, id, repeat, starter, x, y, edges):
        self.id = id
        self.repeat = repeat
        self.starter = starter
        self.x = x
        self.y = y
        self.edges = edges
        # self.data = data

    def send(self):
        pass

    def recive(self):
        pass


def readInputFromCsv():
    initial_data = pd.read_csv('GraphData.csv')
    id = initial_data['id']
    repeat = initial_data['repeat']
    starter = initial_data['starter']
    x = initial_data['x']
    y = initial_data['y']
    edges = initial_data['edges']

    # createTheNodes
    nodes = []
    for i in range(len(id)):
        nodes.append(Node(id[i], repeat[i], starter[i], x[i], y[i], edges[i]))

    return nodes


def creatingGraph(nodes):
    colors_map = []
    G = nx.Graph()
    for i in range(len(nodes)):

        # location
        location = []
        location.append(int(nodes[i].x))
        location.append(int(nodes[i].y))
        G.add_node(nodes[i].id, pos=tuple(location))

        # node color
        if nodes[i].starter == 1:
            colors_map.append("blue")
        else:
            colors_map.append("red")

        # edge
        # edges_array = (nodes[i].edges)
        # help_array = edges_array.split(',')

        # for j in range(len(help_array)):
        #     G.add_edge(i, int(help_array[j]))

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, node_color=colors_map)
    plt.show()


# main

nodes = readInputFromCsv()

creatingGraph(nodes)
