# FODGE - Fast Online Dynamic Graph Embedding

### Contact
********@gmail.com

## Overview

FODGE is a novel dynamic graph embedding algorithm (DGEA) to gradually shift the projection of modified vertices. FODGE optimizes CPU And memory efficacy by separating the projection of the graph densest K-core and its periphery. FODGE then smoothly updates the projection of the remaining vertices, through an iterative local update rule. As such it can be applied to extremely large dynamic graphs. Moreover, it is highly modular and can be combined with any static projection, including graph convolutional networks, and has a few hyperparameters to tune. FODGE obtains a better performance in auxiliary task of link prediction and ensures a limited difference in vertex positions in following time points.

## About This Repo

This repo contains source code of the FODGE dynamic graph embedding algorithm. 

### The Directories

- `datasets` - Examples of datasets files
- `fodge` - The main files to run the FODGE framework
- `GEA` - State-of-the-art static graph embedding algorithms implementations, currently [node2vec](https://arxiv.org/abs/1607.00653)/[GF](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40839.pdf)/[HOPE](https://www.kdd.org/kdd2016/papers/files/rfp0184-ouA.pdf)/[GCN](https://arxiv.org/abs/1609.02907)/[GAE](https://arxiv.org/abs/1611.07308).
- `evaluation_tasks` - Implementation of temporal link prediction task + main file to calculate the embedding and evaluate performance

#### Notes:
- The implementations of GF and HOPE were taken from [GEM toolkit](https://github.com/palash1992/GEM)
- Node2vec is implemented using [node2vec public package](https://github.com/eliorc/node2vec)
- The implementation of GCN was taken from their [public github repository](https://github.com/tkipf/pygcn)
- The implementation of GAE was taken from their [public github repository](https://github.com/tkipf/gae)

## Dependencies
- python >=3.6.8
- numpy >= 1.18.0
- scikit-learn >= 0.22.1
- heapq
- node2vec==0.3.2
- networkx==1.11
- scipy >= 1.41
- pytorch==1.7.0
- matplotlib==3.1.3
- pandas >= 1.0.5
- tensorflow == 2.4.1
- keras == 2.4.3

## Cloning This Repo

If this repository is cloned as a pycharm project, one needs to make all the directories as sources directories.

## Datasets
- Facebook
- Facebook Friendships
- Facebook Wall Posts
- DBLP
- Math
- Enron
- Wiki Temporal

**Note:** All the datasets used can be found in this [google drive link](https://drive.google.com/drive/folders/15tlgyf3GO8s8HjCsd5S5zQ7_n28DafA7?usp=sharing) in the required format. 

If you use one of these datasets, all you have to do is choose the dataset (see name of directories) and put the appropriate `.txt` file in `datasets`directory. 

If you want to use your own dataset, you should follow this format: <br/>
Give a single `.txt` file where each row contains 3/4 columns in the form: <br/>
- **For un-weighted graphs:** from_id to_id time (e.g. 1 2 0 means there is an edge between vertices 1 and 2 at time 0).
- **For weighted graphs:** from_id to_id weight time (e.g. 1 2 0.5 0 means there is an edge of weight 0.5 between vertices 1 and 2 at time 0).
- 
If the provided dataset is in this format, you can put it as it is in the `datasets` directory and use the `data_loader` function that is in `fodge/load_data`. <br/>
If it is not, you should build a data loader function that will convert it to this form. 

## How To Run?

To embed your temporal network with FODGE, you have to provide a `.txt` file representing the network and place it in the `datasets` directory (as explained above).

### Embedding

### Temporal Link Prediction
If you want to perform temporal link prediction task, you must provide non edges file:
"evaluation_tasks/non_edges_{name_of_dataset}" - A csv file which consists of two columns: node1, node2, time ; where there is no edge between them (csv file has no title).
In order to produce such file, you can go to `evaluation_tasks/calculate_non_edges.py`, and follow the instructions there. In addition, you can see the example file here.
