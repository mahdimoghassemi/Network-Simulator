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


# main
readInputFromCsv()
