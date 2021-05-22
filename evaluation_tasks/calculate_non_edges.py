import __init__
import itertools as IT
import csv
import json
import random
import os
import networkx as nx
from datetime import datetime
from fodge.load_data import *


def create_graphs(dict_snapshots):
    """
    From dictionary of times and edges for each time, returen a list of static graphs for each snapshot, list of
    nodes of each graph and list of remaining nodes.
    """
    keys = list(dict_snapshots.keys())
    g_list = []
    for i in range(len(keys)):
        G = nx.DiGraph()
        G.add_edges_from(dict_snapshots[keys[i]])
        H = G.to_undirected()
        g_list.append(H.copy())
        print(i)
    return g_list


def load_graph(func, t):
    """
    Function to load the graph as a dictionary of snapshots
    :param func:
    :param t:
    :return:
    """
    dict_snapshots, dict_weights = func(*t)
    return dict_snapshots, dict_weights


name = "facebook_friendships"
datasets_path = os.path.join("..", "datasets")
func = data_loader
dict_snapshots, dict_weights = load_graph(func, (name, datasets_path))
g_list = create_graphs(dict_snapshots)
times = list(dict_snapshots.keys())

my_list = []
for i in range(len(g_list)):
    g = g_list[i]
    e = g.number_of_edges()
    n = g.number_of_nodes()
    print(n, e)
    nodes = list(g.nodes())
    indexes = random.sample(range(0, len(nodes)), int(len(nodes) * 0.1))
    if i > 50:
        indexes = random.sample(range(0, len(nodes)), int(len(nodes) * 0.05))
    new_nodes = []
    for j in indexes:
        new_nodes.append(nodes[j])
    missing = [pair for pair in IT.combinations(new_nodes, 2) if not g.has_edge(*pair)]
    print(i)
    print(len(missing))
    for pair in missing:
        my_list.append((i, pair[0], pair[1]))

# indexes = random.sample(range(0, len(my_list)), int(len(my_list)))
# new_list = []
# for l in indexes:
#   new_list.append(my_list[l])
csvfile = open('non_edges_{}.csv'.format(name), 'w', newline='')
obj = csv.writer(csvfile)
obj.writerows(my_list)
csvfile.close()
